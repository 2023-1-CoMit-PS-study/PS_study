from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c_num in course:
        temp = []
        for order in orders:
            new_order = sorted(order)
            combi = combinations(new_order, c_num)
            temp += combi
        combi_net = Counter(temp)

        if len(combi_net) > 0 and max(combi_net.values()) > 1:
            for f in combi_net:
                if combi_net[f] == max(combi_net.values()):
                    new_list = [''.join(f)]
                    answer += new_list

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))