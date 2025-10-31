import sys
import io
from collections import defaultdict
import math
import copy


# 작은게 나올 때까지
# 딕셔너리 사용

d, n = map(int, input().split())

oven = list(map(int, input().split()))

pizza = list(map(int, input().split()))

for i in range(1, d):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

pos = d
for p in pizza:

    while pos > 0 and oven[pos-1] < p:
        pos -= 1

    if pos == 0:
        print(0)
        sys.exit()

    pos -= 1

print(pos+1)


