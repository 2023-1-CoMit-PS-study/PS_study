# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p

# 0부터 t * m 까지 범위의 n 진법으로 변환

# 10진수 -> n 진수 변환
def convert (num, base):
    tmp = "0123456789ABCDEF"
    n, mod = divmod(num,base)
    
    if n == 0:
        return tmp[mod]
    else:
        return convert(n, base) + tmp[mod]
    

def solution(n, t, m, p):
    answer = ''
    tmp = ''
    for i in range (0, (t*m)+1):
        tmp += convert(i,n)
        
    while len(answer) < t:
        answer += tmp[p-1]
        p += m

    return answer



print(solution(16,16,2,1))