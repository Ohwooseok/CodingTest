from collections import deque

N, M = map(int, input().split())

what = [list(map(int, input().split())) for _ in range(M)]


direction = [(0,1), (0,-1), (1,0), (-1,0)]


def bfs():
    queue = deque()

    for m in range(M):
        for n in range(N):
            if what[m][n] == 1:
                queue.append((m, n, 0))

    max_day = 0
    while queue:
        x, y, day = queue.popleft()
        max_day = max(max_day, day)
        for ax, ay in direction:
            dx, dy = x+ax, y+ay
            if 0 <= dx < M and 0 <= dy < N:
                if what[dx][dy] == 0:
                    what[dx][dy] = 1
                    queue.append((dx, dy, day + 1))



    for m in range(M):
        for n in range(N):
            if what[m][n] == 0:
                return -1

    return max_day



print(bfs())
