import sys
import io
from collections import deque


N = int(input())
A, B = map(int, input().split())
All = int(input())

graph = [[] for _ in range(N+1)]

for i in range(All):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
distance = [-1] * (N+1)

queue = deque()
queue.append(A)
visited[A] = True
distance[A] = 0

while queue:
    current = queue.popleft()

    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)


print(distance[B])