import sys
import io
from collections import deque
import copy


N = int(sys.stdin.readline())
what = []

for i in range(N):
    what.append(sys.stdin.readline()[:-1])

check = [[False] * N for _ in range(N)] # 정상일 경우 check

color_check = [[False] * N for _ in range(N)] # 적록색약일 경우 check

directions=[(1,0), (-1,0), (0,1), (0,-1)]

def nomal_bfs(a,b,w): # 정상인의 시점
    queue = deque([(a,b)])
    check[a][b] = True

    while queue:
        x,y = queue.popleft()

        for ax, ay in directions:
            dx, dy = ax+x, ay + y

            if 0 <= dx < N and 0 <= dy < N:
                if not check[dx][dy] and what[dx][dy] == w:
                    check[dx][dy] = True
                    queue.append((dx,dy))

def abnomal_bfs(a,b,w): # 적록색약 시점
    queue = deque([(a,b)])
    color_check[a][b] = True

    while queue:
        x,y = queue.popleft()

        for ax, ay in directions:
            dx, dy = ax+x, ay + y

            if 0 <= dx < N and 0 <= dy < N:
                if not color_check[dx][dy]:
                    if w == "R" or w == "G":
                        if what[dx][dy] == "R" or what[dx][dy] == "G":
                            color_check[dx][dy] = True
                            queue.append((dx,dy))
                    else:
                        if what[dx][dy] == w:
                            color_check[dx][dy] = True
                            queue.append((dx,dy))

# 정상인의 시점에서 영역 개수 세기
nomal = 0
for i in range(N):
    for j in range(N):
        if not check[i][j] and what[i][j] == "R":
            nomal_bfs(i,j,"R")
            nomal += 1
        elif not check[i][j] and what[i][j] == "G":
            nomal_bfs(i,j,"G")
            nomal += 1
        elif not check[i][j] and what[i][j] == "B":
            nomal_bfs(i,j,"B")
            nomal += 1

color_what = copy.deepcopy(what)



abnormal = 0

for i in range(N):
    for j in range(N):
        if not color_check[i][j] and what[i][j] == "R":
            abnomal_bfs(i,j,"R")
            abnormal += 1
        elif not color_check[i][j] and what[i][j] == "G":
            abnomal_bfs(i,j,"G")
            abnormal += 1
        elif not color_check[i][j] and what[i][j] == "B":
            abnomal_bfs(i,j,"B")
            abnormal += 1

print(nomal, abnormal)

