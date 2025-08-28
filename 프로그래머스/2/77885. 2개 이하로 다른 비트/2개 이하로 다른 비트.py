def solution(numbers):
    answer = []
    for n in numbers:
        
        if n % 2 == 0:
            answer.append(n+1)
            continue
        
        bn = bin(n)[2:]
        
        # 비트 차이 2 이하의 가장 작은 수를 계산하는 비트 트릭
        xored = n ^ (n + 1)
        bit = xored >> 2
        answer.append(n + 1 + bit)
        
    return answer