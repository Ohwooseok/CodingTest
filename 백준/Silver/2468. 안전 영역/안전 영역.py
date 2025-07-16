import sys
import io
from collections import deque


n = int(input())
flood = []
grid = []

for _ in range(n):
    flood.append([])

for i in range(n):
    for j in range(n):
        flood[i].append(0)



for _ in range(n):
    grid.append(list(map(int, input().split())))



directions = [(1,0), (-1,0), (0,1), (0,-1)]


max_height = 0
for i in range(n):
    max_height = max(max_height, max(grid[i]))



def first_bfs(sx,sy,rain, check):
    queue = deque([(sx,sy)])
    check[sx][sy] = True
    while queue:
        x, y = queue.popleft()

        for ax, ay in directions:
            dx, dy = ax + x, ay + y
            if 0 <= dx < n and 0 <= dy < n :
                if grid[dx][dy] > rain and not check[dx][dy]:
                    check[dx][dy] = True
                    queue.append((dx,dy))

max_safe = 0

for r in range(max_height+1):
    check = [[False] * n for _ in range(n)]
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j] and grid[i][j] > r:
                first_bfs(i,j,r,check)
                safe_count += 1

    max_safe = max(max_safe, safe_count)

print(max_safe)


