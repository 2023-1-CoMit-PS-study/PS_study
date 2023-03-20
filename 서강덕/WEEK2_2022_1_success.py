from math import sqrt
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

def k_num(n, k):
    if k == 0:
        return n
    else:
        new_num = ""
        while n > 0:
            new_num += str(n % k)
            n = n // k
        return new_num[::-1]
    
def check_prime(n):
    if n == 1 or n == 0:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if (n % i == 0):
                return False
    return True
def solution(n, k):
    
    count = 0
    number = k_num(n, k)
    numbers = str(number).split("0")
    #print(numbers)
    for i in numbers:
        if i and check_prime(int(i)): ##short circuit evaluation
            count += 1
    
    return count

print(solution(n, k))

#1. n == 0일 때까지 나눈 문자열 더한 후에, k진수 전환을 위해 라이브러리 reverse로 호출
#2. 0을 기준으로 문자열 나누기
#3. 문자열의 원소를 기준으로 i의 check_prime을 확인 -> short circuit evalation 특징을 이용한 "" 빈 문자 확인
#4. 확인한 수가 소수일 때, count += 1
#5. count 출력