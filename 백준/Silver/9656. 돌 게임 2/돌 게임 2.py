N = int(input())

dp = [False] * (N + 1)
dp[0] = True
dp[1] = False
if N >= 2:
    dp[2] = True
if N >= 3:
    dp[3] = False

for i in range(4, N + 1):
    dp[i] = (not dp[i-1]) or (not dp[i-3])

print("SK" if dp[N] else "CY")
