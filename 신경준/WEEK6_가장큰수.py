#우선 순위 -> if 3, 30 3>30 즉, 공백>앞자리 숫자(32까지보단 크다 33 부터는 동률)
#if 4, 45 비교 -> 45 > 4,/////// 4, 43 비교 -> 4 > 43

# 알고리즘 -> 새로운 배열 만들고(기존 배열의 인덱스를 값으로 하는) 앞자리가 가장 큰거 순으로 정렬해줌
# 동률 생길시 위에서 쓴 알고리즘 사용해서 처리해줌


# 다 시도해봤으나 풀리지 않아서 구글링 선택..
#1000미만의 수이므로 3자리로 모두 맞추어 준 후, 정렬 해줌 key = lambda x:x*3가 3번 반복 후 맞추어 주는 행위

def solution(numbers):
    str_numbers = sorted(list(map(str, numbers)), reverse=True, key = lambda x:x*3)
    return str(int("".join(str_numbers)))

