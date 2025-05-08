def solution(n, k):
    result = 0
    # n을 k진수로 변환한 진법 리스트를 반환하는 함수
    def change(number, digit):
        alist = ''
        while number>0:
            
            alist = str(number % digit) + alist
            number = number // digit
            
        return alist
    
    what = change(n,k)
    
   
    # 입력값 리스트 a를 10진수로 변환한 후 소수인지 판단하는 함수
    def check(a):
        
        """
        # int형 진법 문자열을 10진수로 변환하는 코드
        for val in a:
            number = number * digit + val
        """
        
        number = int(a)
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number ** 0.5)+1, 2):
            if number % i == 0:
                return False
        
        return True
        
   
    parts = what.split('0')
    for p in parts:
        if p and check(p):
            result+=1 

    return result