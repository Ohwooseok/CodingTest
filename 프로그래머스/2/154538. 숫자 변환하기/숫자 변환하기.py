from collections import deque

def solution(x, y, n):
    
    dist = [-1] * (y+1)
    dist[x] = 0
    
    queue = deque([x])
    
    while queue:
        cur = queue.popleft()
        if cur == y:
            return dist[cur]

        for what in (cur * 2, cur * 3, cur + n):
            if what <= y and dist[what] == -1:
                dist[what] = dist[cur] + 1
                queue.append(what)
                
    
    
    return -1