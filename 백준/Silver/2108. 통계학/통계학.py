import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nlist = []

for _ in range(n):
    nlist.append(int(input()))

nlist.sort()

total = sum(nlist)

# 산술평균
if total >= 0:
    print(int(total / n + 0.5))
else:
    print(int(total / n - 0.5))

# 중앙값
print(nlist[n // 2])

# 최빈값
cnt = Counter(nlist)
max_cnt = max(cnt.values())
modes = []

for k, v in cnt.items():
    if v == max_cnt:
        modes.append(k)

modes.sort()

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# 범위
print(nlist[-1] - nlist[0])