import sys
import io
from collections import deque



def DP(N):
    if N == 1:
        print(1)
        return
    elif N == 2:
        print(2)
        return
    elif N == 3:
        print(4)
        return
    dp = [0] * (N+1)

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    DP(n)

