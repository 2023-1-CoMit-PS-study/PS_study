def solution(today, terms, privacies):
    year, month, day = today.split(".")
    today_total = int(year) * 12 * 28 + int(month) * 28 + int(day)
    answer = []
    
    terms_dict = dict()
    for t in terms:
        key, value = t.split()
        terms_dict[key] = int(value)*28
    
    
    for p in range (len(privacies)):
        p_dates, case = privacies[p].split()
        p_year, p_month, p_day = p_dates.split(".")
        p_total = int(p_year) * 12 * 28 + int(p_month) * 28 + int(p_day)        
        p_total_days = p_total + terms_dict[case]
        
        if(today_total >= p_total_days):
            answer.append(p+1)
    
    return answer