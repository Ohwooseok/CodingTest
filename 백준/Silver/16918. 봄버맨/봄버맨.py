import sys
import io
from collections import defaultdict
import math
import copy


r, c, n = map(int, input().split())

board = [list(input()) for _ in range(r)]

def boom(b):
    direction = [(1,0), (-1,0),(0,1),(0,-1)]
    new_b = [['O'] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if b[i][j] == 'O':
                new_b[i][j] = '.'

                for dx, dy in direction:
                    ax = i + dx
                    ay = j + dy

                    if 0 <= ax < r and 0 <= ay < c:
                        new_b[ax][ay] = '.'

    return new_b


if n == 1:
    for b in board:
        print(''.join(b))
elif n % 2 == 0:
    for _ in range(r):
        print('O' * c)
else:
    first = boom(board)
    second = boom(first)

    if (n-3) % 4 == 0:
        for f in first:
            print(''.join(f))
    else:
        for s in second:
            print(''.join(s))







