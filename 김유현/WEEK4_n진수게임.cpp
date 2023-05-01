#include <string>
#include <vector>
#include <algorithm>

std::string to_char(int cur){
    if(cur < 10){
        return std::to_string(cur);
    }
    else if(cur == 10) return std::string("A");
    else if(cur == 11) return std::string("B");
    else if(cur == 12) return std::string("C");
    else if(cur == 13) return std::string("D");
    else if(cur == 14) return std::string("E");
    else if(cur == 15) return std::string("F");
}
std::string solution(int n, int t, int m, int p) {
    std::string answer = "";
    std::vector<std::string> sequence;
    
    sequence.push_back(std::string("0"));
    for(int i = 0; i < t * m; ++i){
        int tmp = i;
        std::vector<std::string> one;
        
        while(tmp){
            one.push_back(to_char(tmp % n));
            tmp /= n;
        }
        std::reverse(one.begin(), one.end());
        for(int i = 0; i < one.size(); ++i)
            sequence.push_back(one[i]);
    }
    for(int i = 0; i < t; ++i)
        answer += sequence[i * m + p - 1];
    return answer;
}
