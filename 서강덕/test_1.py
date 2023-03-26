import sys

input = sys.stdin.readline

board = []

n, m, k = map(int, input().split())

for i in range(n):
    board.append(list(map(int, input().split())))

cube = [1, 6, 4, 3, 5, 2]
change_cube = [0, 0, 0, 0, 0, 0]
dx = [1, 0 , 0, -1]
dy = [0, -1, 1, 0]
score = 0
move_x = 0
move_y = 0
direction = 1
clock_direction = 1

def change(u, d, l, r, f, b, direction):
    if direction == 1:
        change_cube = [l, r, d, u, f, b]
    if direction == 2:
        change_cube = [b, f, l, r, u, d]
    if direction == 3:
        change_cube = [r, l, u, d, f, b]
    if direction == 4:
        change_cube = [f, b, l, r, d, u]
    return change_cube

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = 1
                dfs(nx, ny)

def move(x, y, direction):
    if direction == 1:
        if y == m - 1:
            y -= 1
            direction = 3
            return x, y, direction
        y += 1
    if direction == 2:
        if x == n - 1:
            x -= 1
            direction = 4
            return x, y, direction
        x += 1
    if direction == 3:
        if y == 0:
            y += 1
            direction = 1
            return x, y, direction
        y -= 1
    if direction == 4:
        if x == 0:
            x += 1
            direction = 2
            return x, y, direction
        x -= 1
    return x, y, direction

for i in range(k):
    field_sum = 0
    visited = [[0] * m for _ in range(n)]

    move_x, move_y, direction = move(move_x, move_y, direction)
    visited[move_x][move_y] = 1
    dfs(move_x, move_y)
    #print(move_x, move_y, direction)
    
    for x in range(n):
        for y in range(m):
            if visited[x][y] == 1:
                score += board[move_x][move_y]
    
    # for x in range(n):
    #     print(visited[x])

    #print(' ')

    cube = change(cube[0], cube[1], cube[2], cube[3], cube[4], cube[5], direction)

    if board[move_x][move_y] < cube[1]:
        direction += 1
        if direction == 5:
            direction = 1
    if board[move_x][move_y] > cube[1]:
        direction -= 1
        if direction == 0:
            direction = 4
    else:
        continue
    
print(score)

## 1. 경계면 주의하기 0부터 시작할지, 1부터 시작할지 -> 나는 0부터 시작하기
## 2. 주사위 돌릴 때, 규칙 찾기 시간 닥축시키기
## 3. board 배열 작성할 때, x, y 혼동 주의하기
## 4. def return 설정 할때, direction 추가하는 파트 주의하기
## 5. 조건이 거의 없는 문제라 구현에만 시간이 쓰였지만, 시간 복잡도 줄이는 방법도 생각해보기


## 풀이시간 1시간(단체) + 44분(개인)
## 풀이 난이도 63%