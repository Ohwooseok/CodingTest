import sys
import io
from itertools import combinations
from collections import deque
import copy


board = [list(input().strip()) for _ in range(12)]

check = [[False] * 6 for _ in range(12)]


def bfs(x, y, what):
    q = deque()
    direction = [(0,1), (0,-1), (1,0), (-1,0)]
    check[x][y] = True
    q.append((x,y))
    lst = [(x,y)]

    while q:
        dx, dy = q.popleft()
        for ax, ay in direction:
            nx = ax + dx
            ny = ay + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and not check[nx][ny]:
                if board[nx][ny] == what:
                    check[nx][ny] = True
                    q.append((nx,ny))
                    lst.append((nx,ny))

    return lst


def gravity():
    for c in range(6):
        stack = []
        for r in range(11, -1, -1):
            if not board[r][c] == '.':
                stack.append(board[r][c])

        for r in range(11, -1, -1):
            if stack:
                board[r][c] = stack.pop(0)
            else:
                board[r][c] = '.'

result = 0
while 1:
    check = [[False] * 6 for _ in range(12)]
    to_pop = []

    for i in range(12):
        for j in range(6):
            if not board[i][j] == '.' and not check[i][j]:
                group = bfs(i,j, board[i][j])
                if len(group) >= 4:
                    to_pop.append((i,j))
                    to_pop.extend(group)

    if not to_pop:
        break
    else:
        for x, y in to_pop:
            board[x][y] = '.'

    gravity()
    result += 1


print(result)