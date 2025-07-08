from collections import deque, defaultdict


def solution(n, edge):
    
    ver_dict = defaultdict(list)
    
    for a,b in edge:
        ver_dict[a].append(b)
        ver_dict[b].append(a)
    
    check =[-1] * (n+1)
    check[1] = 0
    
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        
        for n in ver_dict[node]:
            if check[n] == -1:
                check[n] = check[node] + 1
                queue.append(n)
        
    max_distance = max(check)

    print(check)
    return check.count(max_distance)