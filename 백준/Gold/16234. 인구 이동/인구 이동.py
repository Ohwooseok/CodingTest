import sys
import io
from collections import deque


N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


direction = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y):
    queue = deque()
    queue.append((x,y))
    union = [(x,y)]
    check[x][y] = True
    total = board[x][y]

    while queue:
        x, y = queue.popleft()

        for dir in direction:
            dx, dy = dir
            ax = x + dx
            ay = y + dy
            if 0 <= ax < N and 0 <= ay < N and not check[ax][ay]:
                if L <= abs(board[x][y] - board[ax][ay]) <= R:
                    queue.append((ax,ay))
                    check[ax][ay] = True
                    union.append((ax,ay))
                    total += board[ax][ay]

    if len(union) >= 2:

        new = total // len(union)
        for u in union:
            x, y = u
            board[x][y] = new
        return True

    return False

day = 0

while 1:
    check = [[False] * N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if not check[i][j] and dfs(i,j):
               moved = True

    if not moved:
        break

    day += 1




print(day)


