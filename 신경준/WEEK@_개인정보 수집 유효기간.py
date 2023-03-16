def solution(today, terms, privacies):
    # terms key value 담아줌
    limit = {}

    todayYear = int(today.split(".")[0])*12*28
    todayMonth = int(today.split(".")[1])*28
    todayDay = int(today.split(".")[2])

    answer = []

    for i in terms:
        limit[i.split(" ")[0]] = int(i.split(" ")[1])

    k = 0
    for j in privacies:
        k += 1
        limitss = j.split(" ")
        limitTerms = limitss[1]
        limitPeriod = limit.get(limitTerms)*28  # 기한 뽑아줌
        # limitYear = int(limitPeriod/12)
        # limitPeriod = limitPeriod%12

        # 날짜 더해주기
        priv = limitss[0].split(".")
        privYear = int(priv[0])*12*28  # priv year
        privMonth = int(priv[1])*28
        privDay = int(priv[2])

        # privMonth += limitPeriod
        # privYear += limitYear

        # if privMonth > 12:
        #     privYear += 1
        #     privMonth = privMonth+limitPeriod - 12

        # 검증(기한 더해준 날자가 today보다 같거나 작을때)
        # if privYear <= todayYear:
        #     if privYear == todayYear:
        #         if privMonth <= todayMonth:
        #             if privMonth == todayMonth:
        #                 if privDay <= todayDay:
        #                     answer.append(k)
        #             else:
        #                 answer.append(k)
        #     else:
        #         answer.append(k)
        if privYear+privMonth+privDay+limitPeriod <= todayYear+todayMonth+todayDay:
            answer.append(k)

    return answer


# 년도로 계산하니 계속 뭔가 오류가 떨어짐.
# 일자로 변경해서 계산하니 해결.....
# 느낀점: 애초에 문제에서 28일이라고 힌트를 주었으니 그 점을 이용해서 풀자.
# 그리고 조건 잘 읽고 푸는 습관 기르기. 이유 => 유효기간이 1~100이하 인데 이걸 안읽어서 초반에 삽질함


solution("2020.01.01", ["Z 3", "D 5"], [
         "2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
