import sys
import io
import math
from collections import defaultdict
from collections import deque
from collections import Counter



# for 문을 한번 돌리고
# 그 안에 for문을 한번 더 돌림

n = int(input())

li = list(map(int, input().split(" ")))
answer = [-1] * n

start = 0

while start < n:
    end = start

    while end + 1 < n and li[end] == li[end+1]:
        end += 1

    if end + 1 < n:
        for i in range(start, end+1):
            answer[i] = end+2

    start = end + 1

print(*answer)

