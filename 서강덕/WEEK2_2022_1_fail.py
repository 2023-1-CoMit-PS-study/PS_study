import sys

input = sys.stdin.readline

n, k = map(int, input().split())

def check_prime(number):
    if number == 1 or number == 0:
        return False
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i == 0):
                return False
    return True

def solution(n, k):
    
    count = 0
    check_number = 0
    check_time = 0

    while (n >= 0):
        if n == 0:
            if check_prime(check_number):
                count += 1
                break
        if (n % k) == 0:
            if check_prime(check_number):
                count += 1
                check_number = 0
                check_time = 0
                n //= k
                continue
            else:
                check_number = 0
                check_time = 0
                n //= k
                continue
        else:
            check_number += (n % k) * 10 ** check_time
            check_time += 1
            n //= k

    return count

print(solution(n, k))