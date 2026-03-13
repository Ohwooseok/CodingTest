import sys
import io
import math
from collections import defaultdict
from collections import deque
from collections import Counter


n = int(input())


ki = []

for _ in range(n):
    ki.append(list(map(int, input().split(" "))))

# 가장 길이가 긴 기둥 찾기
ki.sort()

maxx = -1_000_000_000
max_idx = 0
for i in range(len(ki)):
    x, y = ki[i]

    if y > maxx:
        maxx = y
        max_idx = i


final = 0

cur_x, cur_y = ki[0]

for i in range(1, max_idx+1):

    if cur_y < ki[i][1]:
        final += (ki[i][0] - cur_x) * cur_y

        cur_x = ki[i][0]
        cur_y = ki[i][1]
    else:
        final += (ki[i][0] - cur_x) * cur_y
        cur_x = ki[i][0]

cur_x, cur_y = ki[-1]

for i in range(n-2, max_idx-1, -1):
    if cur_y < ki[i][1]:
        final += (cur_x - ki[i][0]) * cur_y
        cur_x = ki[i][0]
        cur_y = ki[i][1]
    else:
        final += (cur_x - ki[i][0]) * cur_y
        cur_x = ki[i][0]

final += maxx

print(final)



