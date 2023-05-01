
AllList = [0]


def jin(n, k, numCnt):
    # k진법 변환 알고리즘
    lst = []  # 진수 담아
   
    while n > 0:
        insJinsu = int(n % k)
        if insJinsu == 10:
            insJinsu = 'A'
        if insJinsu == 11:
            insJinsu = 'B'
        if insJinsu == 12:
            insJinsu = 'C'
        if insJinsu == 13:
            insJinsu = 'D'
        if insJinsu == 14:
            insJinsu = 'E'
        if insJinsu == 15:
            insJinsu = 'F'
            
        lst.append(insJinsu)
        numCnt += 1
        n = int(n/k)
    lst.reverse()
    for i in range(len(lst)):
        AllList.append(lst[i])
        
    return numCnt
        
def solution(n, t, m, p):
    deg = 1
    numCnt = 0
    
    while numCnt < t*m + p +1:
        numCnt = jin(deg, n, numCnt)
        deg += 1
    
    imsi = p - 1
    imsiList = []
    for i in range(t):
        imsiList.append(AllList[imsi])
        imsi += m
    
    answer = "".join(map(str, imsiList))
    return answer
        

# 튜브가 말해야 하는 숫자만 구하면 되잖아. 사람수, t 이용해서 그 숫자까지의 범위 구해

solution(16, 16, 2, 1)