#include<iostream>
#include<algorithm>
#include<queue>
#define pp std::pair<int, int>

//                >  V  <   ^
const int y[4] = {0, 1, 0, -1};
const int x[4] = {1, 0, -1, 0};
//            앞 위  뒤 밑 왼  오
//             0  1  2  3  4  5
int dice[6] = {2, 1, 5, 6, 4, 3};
int N, M, K, map[25][25];
int cur_r, cur_c, cur_dir, ans;

bool possible(int r, int c){
    return r >= 0 && r < N && c >= 0 && c < M;
}
void roll(int dir){
    int tmp;
    // >  1 5 3 4
    if(dir == 0){
        tmp = dice[4];
        dice[4] = dice[3];
        dice[3] = dice[5];
        dice[5] = dice[1];
        dice[1] = tmp;
    }
    // V  0 1 2 3
    else if(dir == 1){
        tmp = dice[3];
        dice[3] = dice[2];
        dice[2] = dice[1];
        dice[1] = dice[0];
        dice[0] = tmp;
    }
    // <  4 3 5 1
    else if(dir == 2){
        tmp = dice[1];
        dice[1] = dice[5];
        dice[5] = dice[3];
        dice[3] = dice[4];
        dice[4] = tmp;
    }
    // ^ 3 2 1 0
    else if(dir == 3){
        tmp = dice[0];
        dice[0] = dice[1];
        dice[1] = dice[2];
        dice[2] = dice[3];
        dice[3] = tmp;
    }
}
int get_score(int r, int c){
    int cur_val = map[r][c], ret = 1;
    bool visited[25][25] = {false,};
    std::queue<pp> que;

    que.push({r, c});
    visited[r][c] = true;

    while(!que.empty()){
        int R = que.front().first, C = que.front().second;

        que.pop();
        for(int i = 0; i < 4; ++i){
            int RR = R + y[i];
            int CC = C + x[i];

            if(possible(RR, CC) && !visited[RR][CC] && map[RR][CC] == cur_val){
                ++ret;
                visited[RR][CC] = true;
                que.push({RR, CC});
            }
        }
    }
    return ret;
}
void step(){
    // phase 1
    if(possible(cur_r + y[cur_dir], cur_c + x[cur_dir])){
        cur_r += y[cur_dir];
        cur_c += x[cur_dir];
        roll(cur_dir);
    }
    else{
        cur_dir = (cur_dir + 2) % 4;
        cur_r += y[cur_dir];
        cur_c += x[cur_dir];
        roll(cur_dir);
    }

    // phase 2
    ans += get_score(cur_r, cur_c) * map[cur_r][cur_c];

    // phase 3
    if(dice[3] > map[cur_r][cur_c])
        cur_dir = (cur_dir + 1) % 4;
    else if(dice[3] < map[cur_r][cur_c])
        cur_dir = (cur_dir - 1 + 4) % 4;
}

int main() {
    scanf("%d %d %d", &N, &M, &K);

    for(int i = 0; i < N; ++i)
    for(int u = 0; u < M; ++u)
        scanf("%d", &map[i][u]);
    
    for(int i = 0; i < K; ++i){
        step();
    }
    printf("%d\n", ans);

    return 0;
}
