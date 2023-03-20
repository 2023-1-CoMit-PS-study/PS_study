def convert(n,k):   # k진수로 변환 함수
    result = ''
    while n > 0:
        n,mod = divmod(n,k)
        result += str(mod)
    
    return result[::-1]
       
def is_prime(num): # 소수 판별 함수
    if(num == 1): return False
    for n in range (2, int(num ** 0.5)+1):
        if(num % n == 0):
            return False
    return True
  
def solution(n,k):
    converted = convert(n,k)
    answer = 0
    answers = []
    temp = ''
    
    for i in range(len(converted)):
        if(converted[i] == '0'):
            if(temp != ''):
                answers.append(int(temp))
                temp = ''
            continue
        else:
            temp += converted[i]
    
    if(temp != ''):
        answers.append(int(temp))
    
    for a in answers:
        if(is_prime(a) == True):
            answer += 1
    
    return answer
    # return len(list(filter(is_prime,answers)))