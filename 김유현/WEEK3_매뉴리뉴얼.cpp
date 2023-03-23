#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

std::map<std::string, int> map[15];

void slicing(std::string str){
    // 문자열이 뒤죽박죽
    std::sort(str.begin(), str.end());

    // 문자열에서 만들 수 있는 길이 2 이상의
    // 모든 부분 문자열 생성
    for(int i = 2; i <= str.size(); ++i){
        int arr[15] = {0,};
        
        for(int u = 0; u < i; ++u)
            arr[u] = 1;
        
        do{
            std::string cur = "";
            
            for(int u = 0; u < str.size(); ++u){
                if(arr[u])
                    cur += str[u];
            }
            if(map[cur.size()].find(cur) == map[cur.size()].end())
                map[cur.size()][cur] = 1;
            else
                map[cur.size()][cur] += 1;
        }while(std::prev_permutation(arr, arr + str.size()));
    }
}

std::vector<std::string> solution(std::vector<std::string> orders, std::vector<int> course) {
    std::vector<std::string> answer;

    // 부분 문자열 생성
    for(int i = 0; i < orders.size(); ++i)
        slicing(orders[i]);
    
    for(int i = 0; i < course.size(); ++i){
        std::map<std::string, int>::iterator it;
        int max = 0;

        // 요리의 수가 같은 코스 요리 중 가장 많이 주문된 건수 찾기
        for(it = map[course[i]].begin(); it != map[course[i]].end(); ++it){
            max = std::max(max, it->second);
        }
        if(max < 2)
            continue;
        
        // 가장 많이 주문된 건수에 대한 코스 요리 answer에 저장
        for(it = map[course[i]].begin(); it != map[course[i]].end(); ++it){
            if(it->second == max)
                answer.push_back(it->first);
        }
    }
    // 문제 요구사항
    std::sort(answer.begin(), answer.end());

    return answer;
}
