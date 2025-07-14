from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    answer = []
    what = defaultdict(list)
    
    for a,b in roads:
        what[a].append(b)
        what[b].append(a)
    
    dist = [-1] * (n+1)
    queue = deque([destination])
    dist[destination] = 0
    
    while queue:
        now = queue.popleft()
        
        for neighbor in what[now]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[now] + 1
                queue.append(neighbor)
                
    answer = [dist[s] for s in sources]     
    
    return answer