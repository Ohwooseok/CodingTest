import sys
import io
from collections import deque
import math
import copy


n, k = map(int, input().split()) # k : 바이러스의 종류

board = [list(map(int, input().split())) for _ in range(n)]

s, x, y = map(int, input().split())

virus_xy = []

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            virus_xy.append([board[i][j], 0, i, j])

virus_xy.sort()

virus_xy = deque(virus_xy)

direction = [(0,1), (0,-1), (1,0), (-1,0)]


while virus_xy:
    virus, sec, hx, hy = virus_xy.popleft()

    if sec == s:
        break

    for dx, dy in direction:
        nx = hx + dx
        ny = hy + dy
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                virus_xy.append([virus, sec+1, nx, ny])

print(board[x-1][y-1])

