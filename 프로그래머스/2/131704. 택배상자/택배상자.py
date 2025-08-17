def solution(order):
    n = len(order)
    support = []
    curr = 1
    roaded = 0
    
    
    for o in order:
        while curr <= n and (curr != o) and (not support or support[-1] != o):

            support.append(curr)
            curr += 1
        
        if curr == o:
            curr += 1
            roaded += 1
        elif support[-1] == o:
            support.pop()
            roaded += 1
        else:
            break
        
        
    
    return roaded