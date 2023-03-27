from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        combis = []
        for menu in orders:
            combi = list(combinations(sorted(menu),i))
            combis += combi
        
        check = Counter(combis)
        if check:
            max_val = max(check.values())
            if max_val > 1:
                for k,v in check.items():
                    if v == max_val:
                        answer.append(''.join(k))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))

# orders 
# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]

# course
# [2,3,4]

# result
# ["AC", "ACDE", "BCFG", "CDE"]