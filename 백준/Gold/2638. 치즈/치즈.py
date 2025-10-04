import sys
import io
from collections import deque


n, m = map(int, input().split()) # 세로, 가로

board = [list(map(int, input().split())) for _ in range(n)]


direction = [(1,0), (-1,0), (0,1), (0,-1)]


def make_air(x, y, b):
    check = [[False] * m for _ in range(n)]
    q = deque()
    q.append((x,y))
    check[x][y] = True
    b[x][y] = 2
    while q:
        dx, dy = q.popleft()
        for ax, ay in direction:
            nx = ax + dx
            ny = ay + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny]:
                    if b[nx][ny] == 0:
                        q.append((nx,ny))
                        b[nx][ny] = 2
                        check[nx][ny] = True
                    if b[nx][ny] == 1:
                        check[nx][ny] = True
    return b


def melt_cheese(lst):

    for i in range(n):
        for j in range(m):
            cnt = 0
            if lst[i][j] == 1:
                for ax, ay in direction:
                    nx = ax + i
                    ny = ay + j
                    if 0 <= nx < n and 0 <= ny < m:
                        if lst[nx][ny] == 2:
                            cnt += 1

            if cnt >= 2:
                lst[i][j] = 0

    return lst

result = 0
while 1:
    ccheck = False
    cur_cheese = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cur_cheese+=1

    if cur_cheese > 0:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 0
        board = make_air(0,0, board)
        board = melt_cheese(board)
        result += 1
    else:
        print(result)
        break






