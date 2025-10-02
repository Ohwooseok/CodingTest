import heapq
import sys
import io
from collections import defaultdict
from collections import deque


N, M = map(int, input().split()) # 주차 공간, 차량의 수

# 칸 번호: 1..N
rate = [0] * (N + 1)
for i in range(1, N + 1):
    rate[i] = int(input().strip())

# 차량 번호: 1..M
weight = [0] * (M + 1)
for i in range(1, M + 1):
    weight[i] = int(input().strip())

# 가장 번호가 작은 빈칸을 빠르게 꺼내기 위한 최소힙
free_slots = list(range(1, N + 1))
heapq.heapify(free_slots)

wait = deque()           # 대기 줄(차량 번호)
pos = [0] * (M + 1)      # 차량이 주차한 칸 번호
revenue = 0



for _ in range(2 * M):
    car = int(input())

    if car > 0: # 차량 입장
        if free_slots:
            where = heapq.heappop(free_slots)
            pos[car] = where
            revenue += rate[where] * weight[car]
        else:
            wait.append(car)

    else:
        x = -car
        s = pos[x] # 이 차량이 쓰던 주차 공간 번호
        pos[x] = 0

        if wait:
            nex = wait.popleft()
            pos[nex] = s
            revenue += rate[s] * weight[nex]
        else:
            heapq.heappush(free_slots, s)

print(revenue)