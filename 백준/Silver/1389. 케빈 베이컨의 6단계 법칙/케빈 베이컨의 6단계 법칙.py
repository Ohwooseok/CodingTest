import sys
import io
from collections import deque


N, M = map(int, input().split())

total = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    total[a].append(b)
    total[b].append(a)

result = 0
min = 1_000_000_000
for i in range(1, N+1):
    dist = [-1] * (N+1)

    queue = deque()
    queue.append(i)
    dist[i] = 1

    while queue:
        cur = queue.popleft()

        for neighbor in total[cur]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[cur]+1
                queue.append(neighbor)

    sum_dist = sum(dist[1:])
    if sum_dist < min:
        min = sum_dist
        result = i

print(result)


