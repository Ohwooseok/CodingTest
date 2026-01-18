import sys

n = int(sys.stdin.readline())
k = sys.stdin.readline().strip()

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if k[i-1] == '1':
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

print(dp[n])
