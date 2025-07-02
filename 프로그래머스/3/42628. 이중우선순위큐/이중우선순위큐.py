def solution(operations):
    answer = []
    real = []
    for i in operations:
        order = i[0]
        
        number = int(i[2:])
        
        if order == "I":
            real.append(number)
        
        else:
            if not real:
                continue
            elif number == 1 :
                max_value = max(real)
                real.remove(max_value)
            elif number == -1 :
                min_value = min(real)
                real.remove(min_value)
                
        
    if not real: # 큐가 비어있으면
        answer.append(0)
        answer.append(0)
    else:
        max_value = max(real)
        min_value = min(real)
        
        answer.append(max_value)
        answer.append(min_value)
                
    
    return answer