from collections import defaultdict

def solution(enroll, referral, seller, amount):
    
    money = {}
    parent = {}
    for e in enroll:
        money[e] = 0
    
    for e, r in zip(enroll, referral):
       
        parent[e] = r
    
    
    for s, a in zip(seller, amount):
        price = a * 100
        index = s
        while 1:
            give = price // 10
            money[index] += price - give
            
            if parent[index] == '-' or give < 1:
                break
            
            price = give
            index = parent[index]

    answer = []
    
    for value in money.values():
        answer.append(value)
    
    return answer