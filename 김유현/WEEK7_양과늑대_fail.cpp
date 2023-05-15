#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <cstring>

// 0: sheep, 1:wolf
int N, wolf, sheep = 1, node[20];
int stk_size, stk[20];
bool visited[20];
std::vector<int> graph[20];
std::vector<int> wolf_list[20];
std::queue<int> starter;
std::set<int> cur_wolf;
std::set<int> cur_sheep;

void BFS(){
    std::queue<int> que;

    starter.push(0);
    visited[0] = true;
    que.push(0);
    cur_sheep.insert(0);

    while(!que.empty()){
        int cur = que.front();

        que.pop();
        for(int i = 0; i < graph[cur].size(); ++i){
            int next = graph[cur][i];

            if(!node[next]){
                visited[next] = true;
                cur_sheep.insert(next);
                starter.push(next);
                que.push(next);
            }
        }
    }
}
void DFS(int idx, std::set<int> tmp){
    for(int i = 0; i < graph[idx].size(); ++i){
        int next = graph[idx][i];

        // 양일 때
        if(!node[next]){
            std::set<int> uni;

            if(!visited[next]){
                cur_sheep.insert(next);
                std::set_union(cur_wolf.begin(), cur_wolf.end(), tmp.begin(), tmp.end(), std::inserter(uni, uni.begin()));
                cur_wolf = uni;
            }
            DFS(next, tmp);
        }
        // 늑대일 때
        else{
            std::set<int> uni;

            std::set_union(cur_wolf.begin(), cur_wolf.end(), tmp.begin(), tmp.end(), std::inserter(uni, uni.begin()));
            if(node[next] && cur_sheep.size() - uni.size() > 1){
                tmp.insert(next);
                DFS(next, tmp);
                tmp.erase(next);
            }
        }
        
    }
}
void wolf_each_sheep(int idx){
    if(!node[idx]){
        for(int i = 0; i < stk_size; ++i)
            wolf_list[i].push_back(stk[i]);
    }
    for(int i = 0; i < graph[idx].size(); ++i){
        int next = graph[idx][i];

        if(node[idx]){
            stk[stk_size++] = idx;
        }
        wolf_each_sheep(next);
        if(node[idx]){
            --stk_size;
        }
    }
}

int solution(std::vector<int> info, std::vector<std::vector<int>> edges) {
    int answer = 0;

    N = info.size();
    for(int i = 0; i < N; ++i)
        node[i] = info[i];
    
    for(int i = 0; i < edges.size(); ++i){
        graph[edges[i][0]].push_back(edges[i][1]);
    }
    wolf_each_sheep(0);
    BFS();
    while(1){
        int prev_size = cur_sheep.size();

        while(!starter.empty()){
            int cur = starter.front();

            starter.pop();
            std::set<int> set;
            DFS(cur, set);
        }
        if(prev_size == cur_sheep.size())
            break;
        
        std::set<int>::iterator it;

        memset(visited, false, sizeof(visited));
        for(it = cur_sheep.begin(); it != cur_sheep.end(); ++it){
            starter.push(*it);
            visited[*it] = true;
        }
    }

    answer = cur_sheep.size();

    return answer;
}
