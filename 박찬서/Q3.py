orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [3]
answer = []

for num in course: 
    together_menu = {}
    variable_dict = {}
    for x in range(num): 
        variable_dict[x] = x

    for order in orders:
        if num <= len(order): 
            n = num-1
            while True:
                    
                while variable_dict[num-1] < len(order): 
                    key = '' 
                    for x in range(len(variable_dict)): 
                        key += order[variable_dict[x]]
                    if key in together_menu:
                          together_menu[key] += 1
                    else:
                        together_menu[key] = 1
                        
                    variable_dict[num-1] += 1
                    
                    
                if variable_dict[n] < len(order):
                        variable_dict[n] += 1

                else:
                    n -= 1
                    if n < 0:
                      break
                    else:
                        variable_dict[n] += 1
                        for x in range(num-1-n):
                            variable_dict[x+1] = variable_dict[x]+1

    print(together_menu)  


