from collections import deque
from collections import defaultdict

def solution(edges):
    
    graph = defaultdict(list)
    indec = defaultdict(int)
    outdec = defaultdict(int)
    
    for a, b in edges:
        graph[a].append(b)
        indec[b] += 1
        outdec[a] += 1
    
    start = 0
    for nxt in graph.keys():
        if indec[nxt] == 0 and outdec[nxt] >= 2:
            start = nxt
    
    visited = set([start])
    
    donut = 0
    mak = 0
    eig = 0
    
    for n in graph[start]:
        nodes = set()
        q = deque([n])
        
        makdae = False
        eight = False
    
        while q:
            s = q.popleft()
            
            nodes.add(s)
            if outdec[s] == 0:
                makdae = True
            if outdec[s] == 2:
                eight = True
            
            for nxt in graph[s]:
                if nxt not in nodes:
                    q.append(nxt)
        
        if makdae:
            mak += 1
        elif eight:
            eig += 1
        else:
            donut += 1
        
        visited = set(nodes)
            
            
    
    answer = [start, donut, mak, eig ]
    return answer