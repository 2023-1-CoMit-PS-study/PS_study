import math


def solution(n, k):
    # k진법 변환 알고리즘
    lst = []  # 진수 담아줌
    cnt = 0
    while n > 0:
        lst.append(int(n % k))
        n = int(n/k)
    lst.reverse()
    kjinsu = "".join(map(str, lst))

    nList = []
    for i in kjinsu:
        if i == '0':
            if len(nList) == 0:
                continue
            if isPrime(int("".join(map(str, nList)))):
                cnt += 1
            nList.clear()
        else:
            nList.append(i)
    if len(nList) > 0:
        if isPrime(int("".join(map(str, nList)))):
            cnt += 1
    return cnt


def sosu(a):  #처음에 생각했던 소수 판별 알고리즘 but, 시간초과 ㅠㅠ
    if a == 1:
        return False
    if a == 2:
        return True
    for i in range(2, a):
        if a % i == 0:
            return False  # 소수
    return True  # 소수 아님


def isPrime(n): #검색해서 찾아낸 알고리즘 소수판별은 앞으로 이런식으로
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#=========================생각했던 과정===========================

# 고려해야 될 요소
# 1. k진법으로 어떻게 변환하는가?
# 2. 소수인걸 판별하는 알고리즘

# 수도 코드->
# 1. 주어진 수를 K진법으로 변환
# 2. P 아무것도 없는 경우-> 고려(0 포함 X)

# 리스트 돌면서 0 나오기 전 까지 숫자들 담아줌.
# 0 나오면 담아준 숫자 소수 판별
# 담아준거 비우고 다시 0 나오기 전까지 판별
# 반복문에 끝에서는 무조건 소수 판별

# # 4개의 경우를 나눠서 판단...?


# # 소수판별 알고리즘 자기자신과 1로만 나누어 져야함
# a = 26

# # 소수 판별 알고리즘
# for i in range(2, a):
#     if a % i == 0:
#         print(str(i)+': 소수X')
#         break

# # k진법 변환 알고리즘
# b = 10
# k = 3
# lst = []

# while b > 0:
#     lst.append(int(b % k))
#     b = int(b/k)
#     print(b)
# lst.reverse()
# print(lst)
