import sys
import io
import copy


modes = {
    1 : [[(0,1)], [(1,0)], [(0,-1)], [(-1,0)]],
    2 : [[(0,1), (0,-1)], [(1,0), (-1,0)]],
    3 : [[(0,1), (-1,0)], [(0,-1), (-1,0)], [(0,-1), (1,0)], [(0,1), (1,0)]],
    # 4번은 4가지
    4 : [[(-1,0), (0,1), (1,0)],   # 위, 오른쪽, 아래 (←만 제외)
         [(0,1), (1,0), (0,-1)],   # 오른쪽, 아래, 왼쪽 (↑만 제외)
         [(1,0), (0,-1), (-1,0)],  # 아래, 왼쪽, 위 (→만 제외)
         [(-1,0), (0,-1), (0,1)]], # 위, 왼쪽, 오른쪽 (↓만 제외)
    5 : [[(0,1), (0,-1), (1,0), (-1,0)]]
}
n, m = map(int, input().split()) #세로, 가로

board = [list(map(int, input().split())) for _ in range(n)]

cctv = []

for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] < 6:
            cctv.append((i,j,board[i][j]))

def watch(x, y, dir, temp):
    nx, ny = x, y
    dx, dy = dir
    while 1:
        nx += dx
        ny += dy
        if not (0 <= nx < n and 0 <= ny < m):
            break
        if temp[nx][ny] == 6:
            break
        if temp[nx][ny] == 0:
            temp[nx][ny] = '#'
answer = float("inf")

def dfs(depth, arr):
    global answer
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        answer = min(cnt, answer)
        return

    x, y, cct = cctv[depth]
    for ct in modes[cct]:
        temp = copy.deepcopy(arr)
        for c in ct:
            watch(x,y,c,temp)

        dfs(depth+1, temp)

dfs(0, board)
print(answer)