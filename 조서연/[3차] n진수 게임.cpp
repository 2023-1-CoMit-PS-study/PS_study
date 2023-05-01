#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

void newNum(string& s, int n, int num, int m, int p, int& count){
    string temp = "";
    
    if(n < 10){
        while(num != 0){
            int res = num % n;
            num /= n;
            temp += to_string(res);
        }
    }else{
        while(num != 0){
            int res = num % n;
            num /= n;
            if(res == 10) temp += 'A';
            else if(res == 11) temp += 'B';
            else if(res == 12) temp += 'C';
            else if(res == 13) temp += 'D';
            else if(res == 14) temp += 'E';
            else if(res == 15) temp += 'F';
            else temp += to_string(res);
        }
    }

    for_each(temp.rbegin(), temp.rend(), [&](char c){
        if(count % m == p){
            s += c; 
        }
        count++;
    });
}

string solution(int n, int t, int m, int p) {
    string answer = "";
    int count = 1;
    
    if(p == 1)
        answer += '0'; 
    p--;
    for(int i = 1; i < 50000000; i++){
        newNum(answer, n, i, m, p, count);
        
        if(answer.size() == t)
            break;
        else if(answer.size() > t){
            int len = answer.size() - t;
            for(int j = 0; j < len; j++)
                answer.pop_back();
            break;
        }
    }
    return answer;
}
