from itertools import combinations


def solution(orders, course):
    answer = []
    # 1. orders에 나온 알파벳들에 대해서 체크해주기
    alpCheck = []
    for i in orders:
        for j in i:
            alpCheck.append(j)

    alpCheck = sorted(list(set(alpCheck)))

    # 2. 나온 알파벳들에 대해서 course에 있는 숫자대로 조합 만들어주기
    for i in course:
        comb = []
        # comb에 course에서 나온 숫자길이 만큼 문자열 담아주기
        comb = list(combinations(alpCheck, i)) # 이부분에서 13, 14, 15 시간초과 남 ㅠㅠ
        print(comb)
        checked = [0 for k in range(len(comb))]  # comb에서 몇번 나왔는지 체크
        for j in orders:
            for k in range(len(comb)):
                numCheck = 0
                tt = list(comb[k])
                for t in tt:
                    if t in j:
                        numCheck += 1
                if numCheck == i:
                    checked[k] += 1

        maxCheck = max(checked)
        for p in range(len(checked)):
            if checked[p] >= 2 and checked[p] == maxCheck:
                answer.append("".join(comb[p]))

    answer = sorted(answer)

    return answer
