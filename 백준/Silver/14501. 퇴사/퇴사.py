d = int(input())
T=[]
P=[]
for _ in range(d):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (d+2)

for i in range(d):
    if i + T[i] <= d:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])

    dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))