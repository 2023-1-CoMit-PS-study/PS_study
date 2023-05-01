from itertools import combinations

def solution(orders, course): 
    answer = []
    for i in course:
        comb = []
        tmpComb = []
        
        for u in orders:
            comb += combinations(list(u), i) #각 주문마다 나올 수 있는 메뉴 조합을 담아줌
            
        for u in range(len(comb)): # 중복 없애주기 위한 작업. (더 효율적인 방법이 있으려나?) 
            stt = "".join(comb[u]) 
            tmpComb.append("".join(sorted(list(stt)))) 
        tmpComb = sorted(list(set(tmpComb))) 

        comb.clear() 

        comb = list(set(tmpComb)) #중복 없애주고 다시 담아줌
        checked = [0 for k in range(len(comb))] # 알파벳이 몇번 나왔는지 체크!
        for j in orders:
            for k in range(len(comb)): 
                numCheck = 0
                tt = list(comb[k])
                for t in tt:
                    if t in j:
                        numCheck += 1
                if numCheck == i:
                    checked[k] += 1
        if len(checked) != 0: #가장많이 나온놈 뽑아
            maxCheck = max(checked)
        else:
            maxCheck = -1

        for p in range(len(checked)):
            if checked[p] >= 2 and checked[p] == maxCheck:
                answer.append("".join(comb[p]))

    answer = sorted(answer)

    return answer
