import sys
import io
import math
from collections import defaultdict
from collections import deque
from collections import Counter
from itertools import combinations
import copy



n, m = map(int, input().split())

what = []
for _ in range(n):
    what.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if what[i][j] == 1:
            house.append((i,j))
        elif what[i][j] == 2:
            chicken.append((i,j))


def distance(i,j,k,l):
    return abs(i-k) + abs(j-l)

def chicken_distance(h,c):

    result = 0

    for i,j in h:
        mini = 1_000_000_000
        for k,l in c:
            mini = min(mini, distance(i,j,k,l))


        result += mini

    return result

mini = 1_000_000_000
for hc in combinations(chicken, m):

    mini = min(mini, chicken_distance(house,hc))

print(mini)