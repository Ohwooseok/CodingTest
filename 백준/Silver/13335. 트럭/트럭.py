import sys
import io
from collections import deque

n, w, l = map(int, input().split())
# 트럭 수, 다리의 길이, 다리의 최대 하중

truck = list(map(int, input().split()))


dari = deque([0] * w)
time = 0
cur_weight = 0

while truck or cur_weight > 0 :

    time += 1
    now = dari.popleft() # 다리를 빠져나간 트럭
    cur_weight -= now

    if truck and sum(dari) + truck[0] <= l:
        move = truck.pop(0)
        dari.append(move)
        cur_weight += move
    else:
        dari.append(0)

    if sum(dari) == 0:
        break
print(time)

