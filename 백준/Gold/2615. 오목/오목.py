import sys
import io
from collections import deque
import math
import copy


board = [list(map(int, input().split())) for _ in range(19)]

direction = [(0,1), (1,0), (1,1), (-1,1)]  # ✅ 중복 방지 4방향만


def check(dx, dy, i, j, color):
    le = 1
    startX = i
    startY = j

    px = i - dx
    py = j - dy
    if 0 <= px < 19 and 0 <= py < 19 and board[px][py] == color:
        return []

    while 1:
        i = i + dx
        j = j + dy

        if 0 <= i < 19 and 0 <= j <19:

            if board[i][j] == color:
                le += 1
                continue
            else:
                break
        else:
            break

    if le == 5 :
        return [startX, startY, color]
    else:
        return []


for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            for ax, ay in direction:
                A = check(ax, ay, i, j, board[i][j])
                if not A:
                    continue
                else:
                    print(A[2])
                    print(A[0]+1, A[1]+1)
                    sys.exit()

print(0)