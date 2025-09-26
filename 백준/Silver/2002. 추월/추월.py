import sys
import io
from collections import deque

n = int(input())

arrive = []
for i in range(n):
    arrive.append(input())

dochak = []
for i in range(n):
    dochak.append(input())

arrive_queue = deque(arrive)
visited = []
result = 0
for d in dochak:

    while arrive_queue and arrive_queue[0] in visited:
        arrive_queue.popleft()

    if arrive_queue[0] == d:
        arrive_queue.popleft()

    else:
        result += 1
        visited.append(d)

print(result)