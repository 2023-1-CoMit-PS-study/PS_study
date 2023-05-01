def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert(q, base) + T[r] if q else T[r] #결과 = A if 조건 else B, 조건이 True면 A, False면 B


def solution(n, t, m, p):
    answer = ''
    totalString = ''
    num = 0
    while (len(totalString)<(t*m)):
        totalString += str(convert(num, n))
        num += 1 
    
    print(totalString)
    for x in range(t):
        answer += totalString[(x*m)+(p-1)]
    
    return answer
