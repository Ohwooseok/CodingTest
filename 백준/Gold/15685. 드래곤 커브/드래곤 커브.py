import sys
import io
from collections import deque


n = int(input())
check = [[0] * 101 for _ in range(101)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for _ in range(n):
    x, y, d, g = map(int, input().split())

    direction = [d]
    for _ in range(g):
        for i in range(len(direction)-1 , -1, -1):
            direction.append((direction[i] + 1) % 4 )

    check[y][x] = 1

    for d in direction:
        nx = x + dx[d]
        ny = y + dy[d]
        check[ny][nx] = 1
        x, y = nx, ny

count = 0
for i in range(100):
    for j in range(100):
        if check[i][j] and check[i+1][j] and check[i][j+1] and check[i+1][j+1]:
            count+=1

print(count)