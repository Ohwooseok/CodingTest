import sys
from collections import deque
from itertools import combinations
import copy
import io

N, M = map(int, sys.stdin.readline().split())

what = []
for i in range(N):
    what.append(list(map(int, sys.stdin.readline().split())))


empty_space = []
for i in range(N):
    for j in range(M):
        if what[i][j] == 0:
            empty_space.append((i,j))


def spread_virus(x,y,lab):
    queue = deque([(x,y)])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        x, y = queue.popleft()

        for ax, ay in directions:
            dx, dy = x + ax, y + ay

            if 0 <= dx < N and 0 <= dy < M:
                if lab[dx][dy] == 0:
                    lab[dx][dy] = 2
                    queue.append((dx,dy))

max_what = []

for walls in combinations(empty_space, 3):
    count = 0 # 안전 영역 개수
    fake_what = copy.deepcopy(what)
    for w in walls:
        fake_what[w[0]][w[1]] = 1


    for i in range(N):
        for j in range(M):
            if fake_what[i][j] == 2:
                spread_virus(i,j, fake_what)


    for i in range(N):
        for j in range(M):
            if fake_what[i][j] == 0:
                count += 1

    max_what.append(count)

print(max(max_what))
