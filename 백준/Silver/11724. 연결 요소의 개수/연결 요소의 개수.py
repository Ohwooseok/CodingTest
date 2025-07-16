from collections import deque
import sys


# N 정점 개수, M 간선 개수
N, M =  map(int, sys.stdin.readline().split())

check = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    check[a].append(b)
    check[b].append(a)

visited = [False] * (N+1)

def bfs(node):
    queue = deque([node])
    visited[node] = True

    while queue:
        q = queue.popleft()
        for neigh in check[q]:
            if not visited[neigh]:
                visited[neigh] = True
                queue.append(neigh)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)