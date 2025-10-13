import sys
import io
from collections import deque
from collections import defaultdict
import math
import copy

answer = float('-inf')
n = int(input())
what = input().strip()

def operate(cur, next, op):
    if op == "+":
        return cur + next
    elif op == "-":
        return cur - next
    elif op == "*":
        return cur * next

def dfs(idx, curr):
    global answer

    if idx >= len(ops):
        answer = max(answer, curr)
        return

    next_val= operate(curr, number[idx+1], ops[idx])
    dfs(idx+1, next_val)

    if idx + 1 < len(ops):
        Gual = operate(number[idx+1], number[idx+2], ops[idx+1])
        next_val = operate(curr, Gual, ops[idx])
        dfs(idx+2, next_val)




ops = []
number = []

for i in range(n):
    if i % 2 == 0:
        number.append(int(what[i]))
    else:
        ops.append(what[i])


dfs(0, number[0])
print(answer)