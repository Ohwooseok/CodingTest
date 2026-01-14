import sys
import io


MOD = 1_000_000_000

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n + 1)]


for d in range(1, 10):
    dp[1][d] = 1

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1] % MOD
    dp[i][9] = dp[i - 1][8] % MOD

    for d in range(1, 9):
        dp[i][d] = (dp[i - 1][d - 1] + dp[i - 1][d + 1]) % MOD

print(sum(dp[n]) % MOD)