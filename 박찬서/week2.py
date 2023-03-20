import math

def is_prime_num(n):
    if  n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    global str
    answer = 0
    conversion = []

    while (n > k):
        conversion.insert(0, str(n % k))
        n = int(n / k)

    conversion.insert(0, str(n))

    str = ''.join(conversion)

    n_list = str.split(sep='0')
    n_list = list(filter(None, n_list))

    for x in n_list:
        if is_prime_num(int(x)):
            answer += 1

    return answer
