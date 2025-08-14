def solution(numbers):
    def can_make(n):
        b = bin(n)[2:]
        
        L = len(b)
        size = 1
        
        while size < L:
            size = size * 2 + 1
        
        s= b.rjust(size, '0')
        
        def check(a):
            if len(a) == 1:
                return True
            
            mid = len(a) // 2
            root = a[mid]
            left = a[:mid]
            right = a[mid+1:]
            
            if root == '0':
                if '1' in left or '1' in right:
                    return False
            
            return check(left) and check(right)
        return 1 if check(s) else 0

            
    
    return [can_make(n) for n in numbers]