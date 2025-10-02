import sys
import io
from collections import deque


n, m = map(int, input().split()) # 열, 행

cheese = [list(map(int, input().split())) for _ in range(n)]

direction = [(0,1), (0,-1), (1,0), (-1,0)]


def dfs():
    q = deque()
    check = [[False] * m for _ in range(n)]
    melt = []
    q.append((0,0))
    check[0][0] = True

    while q:
        x, y = q.popleft()

        for dx, dy in direction:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny]:
                    if cheese[nx][ny] == 0:
                        check[nx][ny] = True
                        q.append((nx,ny))
                    elif cheese[nx][ny] == 1:
                        melt.append((nx, ny))
    return melt

ed_cheese = 0
hour = 0
while 1:

    cur_cheese = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                cur_cheese += 1

    if cur_cheese != 0: # 치즈가 있으면
        ed_cheese = cur_cheese
        melt_list = dfs()

        for x, y in melt_list:
            cheese[x][y] = 0

        hour += 1

    else: # 치즈가 없으면
        print(hour)
        print(ed_cheese)
        break



