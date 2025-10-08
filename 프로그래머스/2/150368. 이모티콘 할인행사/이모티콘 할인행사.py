from itertools import product

def solution(users, emoticons):
    
    discount = [10, 20, 30, 40]
    
    answer_total_price = float('-inf')
    answer_plus_emo = float('-inf')
    
    for d in product(discount, repeat = len(emoticons)):
        
        total_price = 0
        plus_emo = 0
        
        for user_disc, user_price in users:
            user_total_price = 0
            for i in range(len(emoticons)):
                if user_disc <= d[i]: # 유저 할인 확률 이상이면
                    user_total_price += emoticons[i] * (1 - d[i] * 0.01) # 할인 가격만큼 user_total_price 증가
                else:
                    continue
            if user_total_price >= user_price:
                plus_emo += 1
            else:
                total_price += user_total_price
        
        if answer_plus_emo < plus_emo:
            answer_plus_emo = plus_emo
            answer_total_price = total_price
        elif answer_plus_emo == plus_emo:
            if answer_total_price < total_price:
                answer_total_price = total_price
                continue
            else:
                continue
                
            
    
    answer = []
    answer.append(answer_plus_emo)
    answer.append(answer_total_price)
    return answer