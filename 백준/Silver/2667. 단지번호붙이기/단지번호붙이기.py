from collections import deque



directions = [(1,0), (-1,0), (0,1), (0,-1)]



N = int(input())

grid = [list(map(int, input())) for _ in range(N)]
check = [[False] * N for _ in range(N)]


def bfs(a,b):

    queue = deque([(a,b)])
    house_count = 1
    check[a][b] = True

    while queue:
        x, y = queue.popleft()

        for px, py in directions:
            dx, dy = x+px, y+py

            if 0 <= dx < N and 0 <= dy < N:
                if not check[dx][dy] and grid[dx][dy] == 1:
                    check[dx][dy] = True
                    queue.append((dx,dy))
                    house_count += 1
    return house_count

size = []

for i in range(N):
    for j in range(N):
        if not check[i][j] and grid[i][j] == 1:
            size.append(bfs(i,j))

print(len(size))
size.sort()

for s in size:
    print(s)
