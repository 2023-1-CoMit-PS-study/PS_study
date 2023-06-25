#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <cstring>

// 0: sheep, 1:wolf
int ans;
bool visited[20];

void DFS(int sheep, int wolf, std::vector<int> &info, std::vector<std::vector<int>> &edges){
    if(sheep > wolf){
        ans = std::max(ans, sheep);
    }
    else
        return;
    
    for(int i = 0; i < edges.size(); ++i){
        if(visited[edges[i][0]] && !visited[edges[i][1]]){
            visited[edges[i][1]] = true;
            if(!info[edges[i][1]])
                DFS(sheep + 1, wolf, info, edges);
            else
                DFS(sheep, wolf + 1, info, edges);
            
            visited[edges[i][1]] = false;
        }
    }
}

int solution(std::vector<int> info, std::vector<std::vector<int>> edges) {
    int answer = 0;

    visited[0] = true;
    DFS(1, 0, info, edges);
    answer = ans;

    return answer;
}
