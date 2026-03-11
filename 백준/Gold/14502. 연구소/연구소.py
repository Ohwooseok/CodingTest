import sys
import io
import math
from collections import defaultdict
from collections import deque
from collections import Counter
from itertools import combinations
import copy



n, m = map(int, input().split())

lab = []

for _ in range(n):
    lab.append(list(map(int, input().split())))

safe_place = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            safe_place.append((i,j))

def spread_virus(x,y,labb):

    direction = [(1,0), (-1,0), (0,-1), (0,1)]
    q = deque([])
    q.append((x,y))

    while q:
        ax, ay = q.popleft()

        for dx, dy in direction:
            nx, ny = ax + dx, ay + dy

            if 0 <= nx < n and 0 <= ny < m:
                if labb[nx][ny] == 0:
                    q.append((nx,ny))
                    labb[nx][ny] = 2

max_count = []
for wall in combinations(safe_place, 3):
    count = 0
    copy_lab = copy.deepcopy(lab)

    for w in wall:
        copy_lab[w[0]][w[1]] = 1


    for i in range(n):
        for j in range(m):
            if copy_lab[i][j] == 2:
                spread_virus(i,j,copy_lab)


    for i in range(n):
        for j in range(m):
            if copy_lab[i][j] == 0:
                count += 1

    max_count.append(count)

print(max(max_count))