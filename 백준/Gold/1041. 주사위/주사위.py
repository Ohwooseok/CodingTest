import sys
import io
from collections import deque
import math
import copy


n = int(input())
dice = list(map(int, input().split()))

if_layer2 = [[0,1], [0, 2], [0, 4], [0, 3],
             [1,3], [1,5], [1,2], [5,3],
             [5, 4], [5,2], [3,4], [4,2]
             ]

min_layer1 = min(dice)

if_layer3 = []
for a in [0,5]:
    for b in [1,4]:
        for c in [2,3]:
            if_layer3.append([a,b,c])



min_layer2 = min( dice[a] + dice[b] for a,b in if_layer2)
min_layer3 = min( dice[a] + dice[b] + dice[c] for a,b,c in if_layer3)

result = 0
if n == 2:
    result += min_layer3 * 4 + min_layer2 * 4
elif n == 1:
    result += sum(dice) - max(dice)
else:
    layer3 = 4
    layer2 = 8 * n - 12
    layer1 = (n-2)**2 + 4*(n-2)*(n-1)


    result = layer3 * min_layer3 + layer2 * min_layer2 + layer1 * min_layer1

print(result)

