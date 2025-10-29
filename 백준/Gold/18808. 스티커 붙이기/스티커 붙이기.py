import sys
import io
from collections import deque



def rotate(s):
    R = len(s)
    C = len(s[0])

    new_s = [[0] * R for _ in range(C)]

    for i in range(R):
        for j in range(C):
            new_s[j][R-i-1] = s[i][j]

    return new_s

def can_place(board, sticker, sr, sc):
    N, M = len(board), len(board[0])
    R, C = len(sticker), len(sticker[0])

    if sr + R > N or sc + C > M:
        return False

    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1 and board[sr + i][sc + j] == 1:
                return False

    return True

def place(board, sticker, sr, sc):
    R, C = len(sticker), len(sticker[0])

    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                board[sr + i][sc + j] = 1

def try_attach(board, sticker):
    N, M = len(board), len(board[0])
    R, C = len(sticker), len(sticker[0])

    for i in range(N):
        for j in range(M):
            if can_place(board, sticker, i, j):
                place(board, sticker, i, j)
                return True

    return False

def process_one(board,sticker):
    cur = sticker
    for _ in range(4):
        if try_attach(board, cur):
            return
        cur = rotate(cur)


N, M, K = map(int, input().split())

board = [[0] * M for _ in range(N)]
for _ in range(K):
    n, m = map(int, input().split())

    st = [list(map(int, input().split())) for _ in range(n)]
    process_one(board, st)

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            result += 1

print(result)