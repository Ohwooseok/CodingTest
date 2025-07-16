from collections import deque


N, M = map(int, input().split())

def bfs(n, m, count):
    queue = deque([(n, m, count)])
    visited = set()
    visited.add(n)

    while queue:
        n, m, count = queue.popleft()
        if n == m:
            return count

        else:
            for a in [n-1, n+1, 2*n]:
                if 0 <= a <= 100000 and a not in visited:
                    visited.add(a)
                    queue.append((a,m,count+1))

print(bfs(N,M,0))