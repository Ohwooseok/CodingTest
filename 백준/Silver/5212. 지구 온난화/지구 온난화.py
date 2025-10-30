import sys
import io
from collections import Counter
import copy


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
copy_board = copy.deepcopy(board)
def bfs(x, y, b):
    direction = [(1,0), (-1,0), (0,1), (0,-1)]
    sea_count = 0
    for dx, dy in direction:
        ax = x + dx
        ay = y + dy

        if not (0 <= ax < n and 0 <= ay < m) or board[ax][ay] == '.':
            sea_count+=1

    if sea_count >= 3:
        b[x][y] = '.'

    return b

for i in range(n):
    for j in range(m):
        if board[i][j] == 'X':
            copy_board = bfs(i,j,copy_board)



min_i = float('inf')
max_i = float('-inf')
min_j = float('inf')
max_j = float('-inf')

for i in range(n):
    for j in range(m):
        if copy_board[i][j] == 'X':

            if i < min_i:
                min_i = i
            if i > max_i:
                max_i = i
            if j < min_j:
                min_j = j
            if j > max_j:
                max_j = j


for i in range(min_i, max_i+1):
    print(''.join(copy_board[i][min_j:max_j+1]))

