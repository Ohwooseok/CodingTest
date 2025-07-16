import sys
import io
from collections import deque


n, m, h = map(int, sys.stdin.readline().split())

# n이 행
# m이 열

what = []
check = []
for i in range(h):
    what.append([])
    check.append([])

for i in range(h):
    for j in range(m):
        what[i].append(list(map(int, sys.stdin.readline().split())))
        check[i].append([False] * n)

directions = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]


def bfs():
    queue = deque([])
    alll = True
    for hh in range(h):
        for mm in range(m):
            for nn in range(n):
                if what[hh][mm][nn] == 1:
                    queue.append((nn,mm,hh,0))
                else:
                    alll = False

    if alll:
        return 0

    max_day = 0
    while queue:
        x, y, z, day = queue.popleft()
        # x 가 행
        # y 가 열
        max_day = max(day, max_day)
        check[z][y][x] = True
        for ax, ay, az in directions:
            dx, dy, dz = ax + x, ay + y, az + z

            if 0 <= dx < n and 0 <= dy < m and 0 <= dz < h:
                if not check[dz][dy][dx] and what[dz][dy][dx] == 0:
                    check[dz][dy][dx] = True
                    what[dz][dy][dx] = 1
                    queue.append((dx,dy,dz, day+1))

    for hh in range(h):
        for mm in range(m):
            for nn in range(n):
                if what[hh][mm][nn] == 0:
                    return -1


    return max_day

print(bfs())

