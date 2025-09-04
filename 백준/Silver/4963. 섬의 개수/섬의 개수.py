import sys
import io
from collections import deque

dxx = [-1,1,0,0,1,-1,1,-1]
dyy = [0,0,-1,1,1,-1,-1,1]

def dfs(x,y,visited, dxx, dyy, mapp, w, h):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(8):
            dx = cx + dxx[i]
            dy = cy + dyy[i]
            if 0 <= dx < w and 0 <= dy < h:
                if mapp[dy][dx] == 1 and not visited[dy][dx]:
                    visited[dy][dx] = True
                    queue.append((dx,dy))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    mapp = []
    for _ in range(h):
        mapp.append(list(map(int, input().split())))

    visited = [[False] * w for _ in range(h)]
    count = 0
    for b in range(h):
        for a in range(w):
            if not visited[b][a] and mapp[b][a] == 1:
                dfs(a,b,visited,dxx,dyy,mapp,w,h)
                count+=1

    print(count)


