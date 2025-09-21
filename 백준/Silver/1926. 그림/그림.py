import sys
import io
from collections import deque


N, M = map(int, input().split())

what = [list(map(int, input().split())) for _ in range(N)]

direction = [(1,0), (-1,0), (0,1), (0,-1)]

check = [[False] * M for _ in range(N)]

def bfs(x, y):
    queue = deque()
    check[x][y] = True
    queue.append((x,y))
    hi = 1
    while queue:
        x, y = queue.popleft()
        for ax, ay in direction:
            dx = ax + x
            dy = ay + y

            if 0 <= dx < N and 0 <= dy < M:
                if what[dx][dy] == 1 and not check[dx][dy]:
                    check[dx][dy] = True
                    queue.append((dx,dy))
                    hi += 1
    return hi

count = 0
max_area = 0
for i in range(N):
    for j in range(M):
        if what[i][j] == 1 and check[i][j] == False:
            count += 1
            area = bfs(i,j)
            max_area = max(max_area, area)
print(count)
print(max_area)



