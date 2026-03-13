import sys
import io
import math
from collections import defaultdict
from collections import deque
from collections import Counter
from itertools import combinations
import copy

n, w, L = map(int,input().split(" "))
# n = 트럭의 수, w = 다리의 길이, L : 다리의 최대 하중

truck = list(map(int, input().split(" ")))

bridge = deque([0] * w)

time = 0
cur_weight = 0

while truck or cur_weight > 0:

    time += 1
    now = bridge.popleft()
    cur_weight -= now

    if truck and truck[0] + cur_weight <= L:
        cur_t = truck.pop(0)
        bridge.append(cur_t)
        cur_weight += cur_t
    else:
        bridge.append(0)


    if sum(bridge) == 0:
        break

print(time)


