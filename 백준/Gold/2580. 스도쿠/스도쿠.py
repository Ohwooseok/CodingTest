import sys
import io
input = sys.stdin.readline


board = [list(map(int, input().split())) for _ in range(9)]

zeros = []
row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]

# 초기 세팅
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            zeros.append((i, j))
        else:
            row[i][num] = True
            col[j][num] = True
            box[(i//3)*3 + (j//3)][num] = True

def dfs(idx):
    if idx == len(zeros):
        for r in board:
            print(*r)
        sys.exit(0)

    x, y = zeros[idx]
    b = (x//3)*3 + (y//3)

    for n in range(1, 10):
        if not row[x][n] and not col[y][n] and not box[b][n]:
            board[x][y] = n
            row[x][n] = col[y][n] = box[b][n] = True
            dfs(idx+1)
            board[x][y] = 0
            row[x][n] = col[y][n] = box[b][n] = False

dfs(0)
