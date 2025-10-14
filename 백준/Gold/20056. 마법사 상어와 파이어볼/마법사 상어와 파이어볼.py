import sys
import io
from collections import defaultdict
import math
import copy


n, m, k = map(int, input().split())

what = defaultdict(list)

# m = 질량, d = 방향, s = 속력
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    what[(r,c)].append([m,s,d])

direction = { 0 : (-1,0), 1 : (-1,1), 2: (0,1), 3: (1,1), 4 : (1,0), 5 : (1,-1), 6 : (0,-1), 7: (-1,-1)}

odd_evenn = [0,2,4,6]
no = [1,3,5,7]

def move(wh):
    new_wh = defaultdict(list)
    
    for key, value in wh.items():
        for v in value:
            r,c = key
            m, s, d = v

            # 세로, 가로
            dirX, dirY = direction[d]

            move_r = (r-1 + dirX * s) % n + 1
            move_c = (c-1 + dirY * s) % n + 1
            new_wh[(move_r,move_c)].append([m,s,d])
    
    return new_wh

def odd_even(li):

    if all(l % 2 == 0 for l in li):
        return True
    elif all(l % 2 == 1 for l in li):
        return True
    else:
        return False

def check(wh):
    new_wh = copy.deepcopy(wh)
    for key, value in wh.items():
        if len(value) >= 2:
            sum_m = 0
            sum_s = 0
            all_dir = []
            for v in value:
                m, s, d = v
                sum_m += m
                sum_s += s
                all_dir.append(d)


            new_wh[key] = []

            if math.floor(sum_m/5) == 0:
                continue
            else:
                for i in range(4):
                    if odd_even(all_dir):
                        new_wh[key].append([math.floor(sum_m/5), math.floor(sum_s / len(value)), odd_evenn[i] ])
                    else:
                        new_wh[key].append([math.floor(sum_m/5), math.floor(sum_s / len(value)), no[i] ])
    return new_wh


for _ in range(k):
    what = move(what)
    
    what = check(what)
    

result = 0



for key, value in what.items():

    for v in value:

        result += v[0]

print(result)
