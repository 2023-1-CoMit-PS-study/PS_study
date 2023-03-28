// 잘 안돌아감
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int max_order[11];
vector<string> coursemenu[11];
map<int, map<string, int> > mp;
void DFS(int idx, int cur, int cnt, vector<char> &menu, string course){
    if(cur == cnt){
        int cur_cnt = ++mp[cnt][course];
        if(cur_cnt < 2) return;
        if(max_order[cnt]< cur_cnt  ){
            max_order[cnt] = cur_cnt;
            coursemenu[cnt].push_back(course);
        }
        return;
    }
    for(int i = idx; i < menu.size(); i++){
        DFS(i+1, cur+1, cnt, menu, course+menu[i]);
    }
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    vector< vector<char> > n;
    for(auto str: orders){
        vector<char> temp;
        for(int i = 0; i < str.size(); i++){
            temp.push_back(str[i]);
        }
        sort(temp.begin(), temp.end());
        n.push_back(temp);
    }
    for(int i = 0; i < n.size(); i++){
        for(int j = 0; j < course.size(); j++){
            DFS(0, 0, course[j], n[i], "");
        }
    }
    for(int i = 0; i < course.size(); i++){
        for(auto &w: coursemenu[course[i]]){
            answer.push_back(w);
        }
    }
    sort(answer.begin(), answer.end());
    return answer;
}
