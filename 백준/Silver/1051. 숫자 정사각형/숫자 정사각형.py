import sys
import io
from collections import defaultdict
from collections import deque


n, m = map(int, input().split(" "))

what = []

for _ in range(n):
    what.append(list(map(int, input())))

max_side = 1

for side in range(2, min(n,m) + 1):
    for i in range(0, n-side+1):
        for j in range(0, m-side+1):
            a = what[i][j]

            if what[i][j+side-1] == a and what[i+side-1][j] == a and what[i+side-1][j+side-1] == a:
                max_side = side

print(max_side * max_side)

