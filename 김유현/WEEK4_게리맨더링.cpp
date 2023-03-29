#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

int N, sum, ans = 9999999, people[15];
bool graph[15][15], belong[15];

int bfs(int n){
    int ret = 1;
    bool visited[15] = {false,};
    std::queue<int> que;

    que.push(n);
    visited[n] = true;
    while(!que.empty()){
        int cur = que.front();

        que.pop();
        for(int i = 0; i < 11; ++i){
            if(graph[cur][i] && !visited[i] && belong[n] == belong[i]){
                ++ret;
                que.push(i);
                visited[i] = true;
            }
        }
    }
    return ret;
}

void slice(int t){
    // 한 쪽 선거구의 사람들 총 수
    int a_sum = 0;
    // 한 쪽 선거구의 수
    int a_n = 0;

    for(int i = 0; i < N; ++i){
        if(t & 1){
            belong[i + 1] = true;
            a_sum += people[i];
            ++a_n;
        }
        else{
            belong[i + 1] = false;
        }
        t >>= 1;
    }
    if(a_sum == sum || a_sum == 0)
        return;
    
    // 같은 쪽 선거구에서 갈 수 있는 선거구를
    // 모두 돌았을 때 해당 쪽 선거구의 총 수와
    // 같지 않으면 문제가 있는 것
    for(int i = 1; i <= N; ++i){
        if(belong[i] == true){
            if(bfs(i) != a_n)
                return;
        }
        else{
            if(bfs(i) != N - a_n)
                return;
        }
    }

    ans = std::min(ans, std::abs(sum - a_sum - a_sum));
}

int main() {
    scanf("%d", &N);
    for(int i = 0; i < N; ++i){
        scanf("%d", &people[i]);
        sum += people[i];
    }
    for(int i = 0; i < N; ++i){
        int size;

        scanf("%d", &size);
        for(int u = 0; u < size; ++u){
            int input;

            scanf("%d", &input);
            graph[i + 1][input] = true;
            graph[input][i + 1] = true;
        }
    }
    // 000001 ~ 111110
    for(int i = 1; i < (2 << N) - 2; ++i){
        slice(i);
    }
    printf("%d\n", (ans == 9999999) ? -1 : ans);
    return 0;
}
