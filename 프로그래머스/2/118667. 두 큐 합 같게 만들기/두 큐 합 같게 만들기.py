from collections import deque

def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    goal = sum(queue1) + sum(queue2)
    
    if goal % 2 == 1:
        return -1
    
    limit = len(queue1) * 3
    target = goal // 2
    count = 0
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    while not sum1 == target and count <= limit:
        if sum1 > target:
            q1 = queue1.popleft()
            sum1 -= q1
            queue2.append(q1)
        
        elif sum1 < target:
            q2 = queue2.popleft()
            sum1 += q2
            queue1.append(q2)
        
        count += 1


        
        
    
        
        
        
        
    if sum(queue1) == sum(queue2):
        return count
    else:
        return -1
    