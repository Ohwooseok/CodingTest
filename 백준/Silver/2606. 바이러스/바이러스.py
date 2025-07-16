import sys
import io
from collections import deque
""" test_input = 7
6
1 2
2 3
1 5
5 2
5 6
4 7


sys.stdin = io.StringIO(test_input) """
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



def bfs(start):
    queue = deque([start])
    check = [False] * (N+1)
    check[start] = True
    count = 0

    while queue:
        node = queue.popleft()

        for neigh in graph[node]:
            if not check[neigh]:
                check[neigh] = True
                count += 1
                queue.append(neigh)

    return count

print(bfs(1))
