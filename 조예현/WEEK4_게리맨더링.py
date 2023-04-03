import sys
from itertools import combinations
from collections import deque

def check_connect(area_list): # 선거구 내 구역들이 연결되어 있는지 체크 -> bfs
    visited = []
    que = deque()
    que.append(area_list[0])
    
    while(que):
        value = que.popleft()
        if value not in visited:
            visited.append(value)
        for c in range(1,len(area_list)):
            if area_map[value][area_list[c]] == 1 and area_list[c] not in visited:
                que.append(area_list[c])
    
    return len(visited) == len(area_list) 
    # 탐색한 노드의 갯수와 구역들 조합의 길이가 같다면 연결 = True


def get_count(a_list,b_list): # 인구 수 차이 계산
    a_sum, b_sum = 0,0
    for a in a_list:
        a_sum += people[a]
    for b in b_list:
        b_sum += people[b]
    
    return abs(a_sum-b_sum)
    


n = int(sys.stdin.readline().rstrip())
people = list(map(int,sys.stdin.readline().rstrip().split()))
area_map=[[0 for _ in range(n)] for _ in range(n)]
results = []

for x in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for y in range(1,temp[0]+1):
        area_map[x][temp[y]-1] = area_map[temp[y]-1][x] = 1


area_n = [_ for _ in range (0,n)]
for i in range(1,n//2+1):
    area_as = list(combinations(area_n,i)) # 조합 구하기 위해 combinations 이용
    
    for area_a in area_as:
        area_b = [] # a 구역에 포함되지 않은 구역 => b 구역으로 지정
        for j in range (n):
            if j not in list(area_a):
                area_b.append(j)
        
        # area_a & area_b check connect
        if(check_connect(list(area_a)) and check_connect(area_b)):
            results.append(get_count(list(area_a),area_b))
            
                


if results:
    print(min(results)) # 결과들 중 가장 작은 값 출력
else :
    print("-1")