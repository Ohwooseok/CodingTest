import sys
import io
from itertools import combinations
from collections import deque
import copy


n, m, d= map(int, input().split()) # 세로, 가로

board = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]


def find_enemy(bd, achor_col, D,N,M):
    check = [[False] * m for _ in range(n)]
    q = deque()
    q.append((N-1, achor_col, 1))
    check[N-1][achor_col] = True

    directions = [(0, -1), (-1,0), (0,1) ]

    while q:
        x, y, dist = q.popleft()

        if dist > D:
            break
        if bd[x][y] == 1:
            return (x,y)
        for ax, ay in directions:
            nx, ny = x+ ax, y + ay
            if 0 <= nx < N and 0 <= ny < M and not check[nx][ny]:
                check[nx][ny] = True
                q.append((nx, ny, dist+1))

def simulate(archers, board, N, M, D):
    temp = copy.deepcopy(board)
    kill = 0

    for _ in range(N):
        targets = set()

        for col in archers:
            target = find_enemy(temp, col, D, N, M)
            if target:
                targets.add(target)

        for r, c in targets:
            if temp[r][c] == 1:
                temp[r][c] = 0
                kill += 1

        temp.pop()
        temp.insert(0, [0]*M)

    return kill

max_kill = 0
for archers in combinations(range(m), 3):
    killed = simulate(archers, board, n,m,d)
    max_kill = max(max_kill, killed)

print(max_kill)