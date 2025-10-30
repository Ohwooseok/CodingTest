import sys
import io
from itertools import permutations
import math
import copy


n = int(input())

dice = [list(map(int, input().split())) for _ in range(n)]


pair = [(0,5), (1,3), (2,4)]

def max_find(t, d, l):
    maxx = float('-inf')

    for ll in range(len(l)):
        if ll in (t,d):
            continue

        maxx = max(maxx, l[ll])

    return maxx

result = float("-inf")


for i in range(6):
    down = i
    r = 0
    for j in range(n):
        if j == 0:
            for a, b in pair:
                if a == down:
                    top = b
                    break
                elif b == down:
                    top = a
                    break

            r += max_find(top, down, dice[j])

            down = dice[j][top]
        else:
            down = dice[j].index(down)
            for a, b in pair:
                if a == down:
                    top = b
                    break
                elif b == down:
                    top = a
                    break
            r += max_find(top, down, dice[j])

            down = dice[j][top]

    result = max(result, r)

print(result)






