import sys
import io
from collections import deque


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(1,0), (-1,0), (0,-1), (0,1)]
icebergs = []

for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            icebergs.append((i,j))


def bfs(x, y, checker):
    q = deque([(x,y)])
    checker[x][y] = True
    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] > 0 and not checker[nx][ny]:
                    checker[nx][ny] = True
                    q.append((nx, ny))

result = 0
while 1:

    count = [[0] * M for _ in range(N)]
    for x,y in icebergs:
        for dx,dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                count[x][y] += 1

    new_icebergs = []
    for x,y in icebergs:
        if board[x][y] > 0:
            board[x][y] = max(0, board[x][y]-count[x][y])
            if board[x][y] > 0:
                new_icebergs.append((x,y))
    icebergs = new_icebergs


    result += 1
    checker = [[False] * M for _ in range(N)]
    dong = 0
    for x,y in icebergs:
        if not checker[x][y]:
            bfs(x,y,checker)
            dong += 1


    if dong == 0:
        print(0)
        break
    if dong >=2:
        print(result)
        break


