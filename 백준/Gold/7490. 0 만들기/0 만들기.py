import sys
import io
from collections import deque
import math
import copy


def evaluate(expr):
    expr = expr.replace(" ","")
    return eval(expr)

def dfs(total, idx, expr, result):

    if total == idx:
        if evaluate(expr) == 0:
            result.append(expr)
        return

    for ch in [" ", "+", "-"]:
        dfs(total, idx+1, expr + ch + str(idx+1), result)



n = int(input())

for _ in range(n):
    N = int(input())
    result = []
    dfs(N, 1, "1", result)

    for r in result:
        print(r)
    print()
