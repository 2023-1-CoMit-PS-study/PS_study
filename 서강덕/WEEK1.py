import sys

input = sys.stdin.readline

def solution(today, terms, privacies):
    answer = []
    terms_list = [[0] * 2] * len(terms)
    privacies_list = [[0] * 4] * len(privacies)

    today_list = today.split(".")
    #print(len(terms))
    for i in range(len(terms)):
        terms_list[i] = terms[i].split(" ")

    for i in range(len(privacies)):
        privacies_list[i] = privacies[i].split(".")
        privacies_list[i][2] = privacies_list[i][2].split(" ")
        #privacies_list[i][3] = privacies_list[i][2].split(" ")[1]
        #privacies_list[i][3] = privacies[i].split(" ")[1]


    #print(today_list)
    #print(terms_list)
    #print(privacies_list)

    index = 0

    for priva in privacies_list:
        long_time = 0
        index += 1
        last_year = int(priva[0])
        last_mon = int(priva[1])
        last_day = int(priva[2][0])
        type = priva[2][1]

        for term in terms_list:
            if term[0] == type:
                long_time = int(term[1])

        last_mon += long_time
        #print(last_mon)
        last_day -= 1

        if last_day <= 0:
            last_mon -= 1
            last_day = 28
        
        while (last_mon >= 13):
            last_year += 1
            last_mon -= 12

        #print(last_year, last_mon, last_day)

        if int(today_list[0]) > last_year:
            answer.append(index)
        if int(today_list[0]) == last_year:
            if int(today_list[1]) > last_mon:
                answer.append(index)
            if int(today_list[1]) == last_mon:
                if int(today_list[2]) > last_day:
                    answer.append(index)

    return answer


# print(solution("2020.01.01", ["Z 3", "D 5"], [
#          "2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

print(solution("2022.02.28", ["A 23"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))

# 약관 기간이 12 * n인 경우도 고려해야 됨