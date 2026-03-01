import sys
import io

check = [False] * 10001

for i in range(1, 10001):
    a = i
    d = i
    while a > 0:
        d += a % 10
        a //= 10

    if d <= 10000:
        check[d] = True


for i in range(1, 10001):
    if not check[i]:
        print(i)
