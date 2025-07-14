def solution(sequence):
    purse1, purse2 = [], []
    
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            purse1.append(val)
            purse2.append(-val)
        else:
            purse1.append(-val)
            purse2.append(val)
    
    
    def max_find(arr):
        what_max = arr[0]
        cur_max = arr[0]
        
        for num in arr[1:]:
            what_max = max(num, what_max+num)
            cur_max = max(what_max, cur_max)
        
        return cur_max

    return max(max_find(purse1), max_find(purse2))