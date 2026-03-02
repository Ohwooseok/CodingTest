import sys
import io
from collections import defaultdict



# for 문 쓰고 지금 순서, p, q 저장
# 그 안에 있는 다른 for 문 으로 지금 순서면 continue, 비교해서 k 찾음
# 리스트에 k + 1 저장

n = int(input())
what = []
rank = []
for i in range(n):
    x, y = map(int, input().split())
    what.append([x,y])

for i in range(len(what)):
    x, y = what[i]
    cur = i
    k = 0

    for j in range(len(what)):
        if j == cur:
            continue
        else:
            p, q = what[j]

            if p > x and q > y:
                k += 1

            else:
                continue

    rank.append(k+1)



print(*rank)

