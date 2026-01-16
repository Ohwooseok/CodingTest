import sys

n = int(sys.stdin.readline().strip())

ans = 0
pow3 = 1

while n > 0:
    if n % 2 == 1:
        ans += pow3
    n //= 2
    pow3 *= 3

print(ans)
