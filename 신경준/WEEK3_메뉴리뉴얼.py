from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        comb = []
        tmpComb = []
        
        for u in orders:
            comb += combinations(list(u), i)
            
        for u in range(len(comb)):
            stt = "".join(comb[u])
            tmpComb.append("".join(sorted(list(stt))))
        tmpComb = sorted(list(set(tmpComb)))

        comb.clear()

        comb = list(set(tmpComb))
        checked = [0 for k in range(len(comb))]
        for j in orders:
            for k in range(len(comb)):
                numCheck = 0
                tt = list(comb[k])
                for t in tt:
                    if t in j:
                        numCheck += 1
                if numCheck == i:
                    checked[k] += 1
        if len(checked) != 0:
            maxCheck = max(checked)
        else:
            maxCheck = -1

        for p in range(len(checked)):
            if checked[p] >= 2 and checked[p] == maxCheck:
                answer.append("".join(comb[p]))

    answer = sorted(answer)

    return answer
