#include<iostream>

//                 ^  >  V   <
const int y[4] = {-1, 0, 1, 0};
const int x[4] = { 0, 1, 0,-1};
int N, M, sr, sc, dir, ans;
int room[55][55];

bool possible(int r, int c){
    return r >= 0 && r < N && c >= 0 && c < M;
}
bool is_phase2(){
    int ret = 0;

    for(int i = 0; i < 4; ++i){
        int R = sr + y[i], C = sc + x[i];
        if(possible(R, C) && room[R][C])
            ++ret;
    }
    return (ret == 4) ? true : false;
}

int main() {
    scanf("%d %d\n%d %d %d", &N, &M, &sr, &sc, &dir);
    
    for(int i = 0; i < N; ++i)
    for(int u = 0; u < M; ++u){
        scanf("%d", &room[i][u]);
    }
    while(1){
        // phase 1
        if(room[sr][sc] == 0){
            room[sr][sc] = -1;
            ++ans;
        }
        // phase 2
        if(is_phase2()){
            // phase 2-1
            int R = sr + y[(dir + 2) % 4];
            int C = sc + x[(dir + 2) % 4];

            if(possible(R, C) && room[R][C] != 1){
                sr += y[(dir + 2) % 4];
                sc += x[(dir + 2) % 4];
                continue;
            }
            // phase 2-2
            else
                break;
        }
        // phase 3
        else{
            // phase 3-1
            dir = (dir - 1 + 4) % 4;

            // phase 3-2
            int R = sr + y[dir];
            int C = sc + x[dir];
            
            if(possible(R, C) && !room[R][C]){
                sr += y[dir];
                sc += x[dir];
            }
            // phase 3-3
            continue;
        }
    }
    printf("%d\n", ans);

    return 0;
}
