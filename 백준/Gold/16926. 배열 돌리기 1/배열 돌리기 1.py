import sys
import io
from collections import deque



n, m, r = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]


layer = min(n,m) // 2

for i in range(layer):
    max_n = n - i
    min_m = i
    max_m = m - i
    min_n = i

    what = []

    for j in range(i, max_m):
        what.append(li[min_n][j])

    for j in range(min_n+1, max_n):
        what.append(li[j][max_m-1])

    for j in range(max_m-2, min_m-1, -1):
        what.append(li[max_n-1][j])

    for j in range(max_n-2, min_n, -1):
        what.append(li[j][min_m])

    w = len(what)

    what = deque(what)

    rr = r % w
    
    what.rotate(-rr)


    for j in range(i, max_m):
        li[min_n][j] = what.popleft()

    for j in range(min_n+1, max_n):
        li[j][max_m-1] = what.popleft()

    for j in range(max_m-2, min_m-1, -1):
        li[max_n-1][j] = what.popleft()

    for j in range(max_n-2, min_n, -1):
        li[j][min_m] = what.popleft()


for l in li:
    print(*l)