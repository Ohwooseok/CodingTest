import sys
import io
from collections import deque


test_case = int(input())
for _ in range(test_case):
    N, M, Count = map(int, input().split())

    what = [[] for _ in range(M)]

    for m in range(M):
        for n in range(N):
            what[m].append(0)

    for i in range(Count):
        a, b = map(int, input().split())
        what[b][a] = 1

    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    check = [[False] * N for _ in range(M)]

    level = 0

    def bfs(a,b):
        queue = deque([(a,b)])
        check[a][b] = True


        while queue:
            x, y = queue.popleft()

            for ax, ay in directions:
                dx, dy = x+ax, y+ay
                if 0 <= dx < M and 0 <= dy < N:
                    if not check[dx][dy] and what[dx][dy] == 1:
                        check[dx][dy] = True
                        queue.append((dx,dy))


    for m in range(M):
        for n in range(N):
            if not check[m][n] and what[m][n] == 1:
                bfs(m,n)
                level += 1

    print(level)
