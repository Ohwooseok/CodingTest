import sys
import io
from collections import Counter
from collections import deque
import copy
from copy import deepcopy
from itertools import permutations, combinations



n, m, k = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(n)]
rota = [list(map(int, input().split())) for _ in range(k)]


def rot(r, c, s, li):

    max_n = r + s - 1
    min_n = r - s - 1
    min_m = c - s - 1
    max_m = c + s - 1

  
    layer = min(max_n - min_n + 1,max_m - min_m + 1) // 2

    for i in range(layer):
        max_nn = max_n - i
        min_mm = min_m + i
        max_mm = max_m - i
        min_nn = min_n + i


        what = []

        for j in range(min_mm, max_mm+1):
            what.append(li[min_nn][j])

        for j in range(min_nn+1, max_nn+1):
            what.append(li[j][max_mm])

        for j in range(max_mm-1, min_mm-1, -1):
            what.append(li[max_nn][j])

        for j in range(max_nn-1, min_nn, -1):
            what.append(li[j][min_mm])


        what = deque(what)

        what.rotate(1)


        for j in range(min_mm, max_mm+1):
            li[min_nn][j] = what.popleft()

        for j in range(min_nn+1, max_nn+1):
            li[j][max_mm] = what.popleft()

        for j in range(max_mm-1, min_mm-1, -1):
            li[max_nn][j] = what.popleft()

        for j in range(max_nn-1, min_nn, -1):
            li[j][min_mm] = what.popleft()




    return li

result = float('inf')
for per_ro in permutations(rota, k):
    copy_lis = copy.deepcopy(lis)
    for p in per_ro:
        r, c, s = p
        copy_lis = rot(r,c,s,copy_lis)
    a = min(sum(c) for c in copy_lis)
    result = min(result, a)


print(result)