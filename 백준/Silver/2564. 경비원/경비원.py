import sys
import io
from collections import defaultdict
import math
import copy

x, y = map(int, input().split())

sang_c = int(input())

where = []

for _ in range(sang_c+1):
    dire, w = map(int, input().split())
    if dire == 1:
        where.append([dire, w, y])
    elif dire == 2:
        where.append([dire, w, 0])
    elif dire == 3:
        where.append([dire, 0, y-w])
    elif dire == 4:
        where.append([dire, x, y-w])

dong = where[-1]
dong_dire, dong_x, dong_y = dong
where = where[:sang_c]

total_dul = 2 * x + 2 * y

result = 0

oppo = [(1,2), (3,4), (2,1), (4,3)]

for w in where:
    w_dire, w_x, w_y = w

    if w_dire == dong_dire: # 동일 선상
        hmm = abs(w_x - dong_x) + abs(w_y - dong_y)
        result += min(hmm, total_dul - hmm)
    elif (w_dire, dong_dire) in oppo: # 정반대
        hmm = w_x + w_y + dong_x + dong_y
        result += min(hmm, total_dul - hmm)
    else:
        hmm = abs(w_x - dong_x) + abs(w_y - dong_y)
        result += min(hmm, total_dul - hmm)

print(result)