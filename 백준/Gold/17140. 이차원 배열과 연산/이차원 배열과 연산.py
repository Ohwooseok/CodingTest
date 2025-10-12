import sys
import io
from collections import Counter
from collections import deque
import copy


r, c, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(3)]



def cal_R(A):
    result = []
    max_len = 0
    for row in A:
        counter = Counter(x for x in row if x != 0)
        sorted_row = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for a, b in sorted_row:
            new_row += [a, b]
        max_len = max(max_len, len(new_row))
        result.append(new_row)
    # 패딩
    for i in range(len(result)):
        while len(result[i]) < max_len:
            result[i].append(0)
        if len(result[i]) > 100:
            result[i] = result[i][:100]
    if len(result) > 100:
        result = result[:100]
    return result

def cal_C(home):
    transpose = list(map(list, zip(*home)))
    transpose = cal_R(transpose)
    return list(map(list, zip(*transpose)))

count = 0
while True:
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]) and A[r-1][c-1] == k:
        print(count)
        break
    if count > 100:
        print(-1)
        break

    rows, cols = len(A), len(A[0])
    if rows >= cols:
        A = cal_R(A)
    else:
        A = cal_C(A)
    count += 1