#include <string>
#include <vector>
#include <algorithm>
#define pp std::pair<int, int>

int N, M, ex_arr[10];
std::vector<pp> tmp_ans;
std::vector<std::vector<int>> user;
std::vector<int> emoticon;

void EX(int idx){
    if(idx == M){
        int plus = 0;
        int sum = 0;
        
        for(int i = 0; i < N; ++i){
            int pay = 0;
            
            for(int u = 0; u < M; ++u)
                pay += (ex_arr[u] >= user[i][0]) ? (emoticon[u] / 10) * (10 - ex_arr[u] / 10) : 0;
            
            if(pay >= user[i][1])
                ++plus;
            else
                sum += pay;
        }
        tmp_ans.push_back({plus, sum});
        
        return;
    }
    for(int i = 1; i < 5; ++i){
        ex_arr[idx] = i * 10;
        EX(idx + 1);
    }
}

std::vector<int> solution(std::vector<std::vector<int>> users, std::vector<int> emoticons) {
    std::vector<int> answer;
    
    N = users.size();
    M = emoticons.size();
    user = users;
    emoticon = emoticons;
    
    EX(0);
    
    std::sort(tmp_ans.begin(), tmp_ans.end());
    answer.push_back(tmp_ans[tmp_ans.size() - 1].first);
    answer.push_back(tmp_ans[tmp_ans.size() - 1].second);
    
    return answer;
}
