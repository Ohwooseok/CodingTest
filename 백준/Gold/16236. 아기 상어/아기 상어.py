import sys
import io
from collections import deque

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

direction = [(1,0), (-1,0), (0,1), (0,-1)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_x, shark_y = i, j
            board[i][j] = 0
            break

time = 0
eat_count = 0
shark_size = 2

def dfs(x, y, size):
    q = deque()
    q.append((x,y))
    check = [[-1] * N for _ in range(N)]
    check[x][y] = 0
    fishes = []
    min_dist = float('inf')

    while q:
        ax, ay = q.popleft()

        for dx, dy in direction:
            nx = ax + dx
            ny = ay + dy
            if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == -1:
                if board[nx][ny] > size:
                    continue

                check[nx][ny] = check[ax][ay] + 1

                if 0 < board[nx][ny] < size:
                    dist = check[nx][ny]
                    if dist <= min_dist:
                        min_dist = dist
                        fishes.append((dist,nx,ny))

                q.append((nx,ny))

    if fishes:
        fishes.sort()
        return fishes[0]
    return None

while 1:
    result = dfs(shark_x, shark_y, shark_size)

    if result is None:
        break

    dist, nx, ny = result
    time += dist
    shark_x, shark_y = nx, ny
    board[nx][ny] = 0
    eat_count += 1

    if eat_count == shark_size:
        eat_count = 0
        shark_size += 1

print(time)