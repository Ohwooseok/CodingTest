import sys
import io
from collections import deque

N, M, K = map(int, input().split())

board = [[0] * M for _ in range(N)]

for i in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

directions = [(1,0), (-1,0), (0,1), (0,-1)]
check = [[False] * M for _ in range(N)]


def bfs(x, y):
    q = deque()
    q.append((x,y))
    check[x][y] = True
    what = 1

    while q:
        dx, dy = q.popleft()

        for nx, ny in directions:
            ax = nx + dx
            ay = ny + dy

            if 0 <= ax < N and 0 <= ay < M:
                if  board[ax][ay] == 1 and not check[ax][ay] :
                    check[ax][ay] = True
                    q.append((ax,ay))
                    what += 1

    return what

result = float('-inf')
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not check[i][j]:
            r = bfs(i,j)
            result = max(result, r)

print(result)

