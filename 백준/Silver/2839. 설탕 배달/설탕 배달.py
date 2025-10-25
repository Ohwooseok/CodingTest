import sys
import io
from collections import deque
import math
import copy


n = int(input())

dp = [-1] * (n+1)

dp[3] = 1

if n >= 5:
    dp[5] = 1


for i in range(6, n+1):
    a = dp[i-3]
    b = dp[i-5]

    if a == -1 and b == -1:
        dp[i] = -1
    elif a == -1:
        dp[i] = b+1
    elif b == -1 :
        dp[i] = a + 1
    else:
        dp[i] = min(a,b) + 1

print(dp[n])