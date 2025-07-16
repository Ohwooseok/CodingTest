import sys
import io
from collections import deque


N, M = map(int, input().split())
what = []
for _ in range(N):
        what.append(list(map(int, input())))

check = [[False] * M for _ in range(N)]


direction = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(a,b):
    queue = deque([(a,b)])
    check[a][b] = True
    while queue:
        x, y = queue.popleft()

        for ax, by in direction:
            dx, dy = x + ax, y + by
            if 0 <= dx < N and 0 <= dy < M:
                if not check[dx][dy] and what[dx][dy] == 1:
                    check[dx][dy] = True
                    queue.append((dx,dy))
                    what[dx][dy] = what[x][y] + 1

bfs(0,0)
print(what[N-1][M-1])

