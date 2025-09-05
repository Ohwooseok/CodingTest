import sys
import io
from collections import deque

dxx = [-1, 1, 0, 0]
dyy = [0, 0, -1, 1]


M, N, K = map(int, input().split())

where = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
# N이 가로, M이 세로
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2 ):
            where[y][x] = 1


def bfs(x, y, visited, where, dxx, dyy):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    area_count = 1
    while queue:
        dx, dy = queue.popleft()
        for i in range(4):
            nx = dx + dxx[i]
            ny = dy + dyy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[ny][nx] and where[ny][nx] == 0:
                    queue.append((nx,ny))
                    visited[ny][nx] = True
                    area_count += 1

    return area_count

result = []
count = 0
for y in range(M):
    for x in range(N):
        if not visited[y][x] and where[y][x] == 0:
            result.append(bfs(x,y,visited,where,dxx,dyy))
            count += 1

result.sort()
print(count)
result1 = ' '.join(map(str, result))
print(result1)




