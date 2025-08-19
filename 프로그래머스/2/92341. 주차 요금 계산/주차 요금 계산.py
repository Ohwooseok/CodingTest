from collections import defaultdict
import math

def solution(fees, records):
    # 기본 시간(분), 기본 요금, 단위 시간(분), 단위 요금
    
    ddict = defaultdict(list)
   
    for r in records:
        a = r.split()
        ddict[int(a[1])].append(a[0])
    
    sort_dict = dict(sorted(ddict.items()))
    def to_minute(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m
    def calculate(lst, fees):
        fee = 0
        total = 0
        if len(lst) % 2 == 0: # 입출 내역이 짝이 맞는 경우
            for i in range(0, len(lst), 2):
                total += to_minute(lst[i+1]) - to_minute(lst[i])
                

        elif len(lst) == 1:
            
            total += to_minute("23:59") - to_minute(lst[0])
          
        else:
            for i in range(0, len(lst)-1, 2):
                total += to_minute(lst[i+1]) - to_minute(lst[i])
                
            
            total += to_minute("23:59") - to_minute(lst[-1])
                
            
                
        if total <= fees[0]: # 기본 시간 이하
            return fees[1]
        else: # 기본 시간 초과
            over = total - fees[0]
            return fees[1] + math.ceil(over / fees[2]) * fees[3]
        return fee
            
    
    answer = []
    for key, value in sort_dict.items():
        answer.append(calculate(value,fees))
        
                    
                
            
        
    

    return answer