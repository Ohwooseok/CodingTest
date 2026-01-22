import sys
import io
from collections import deque


N = int(input())

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    F = [0] * (N+1)
    F[0] = 0
    F[1] = 1
    for i in range(2, N+1):
        F[i] = F[i-1] + F[i-2]

    print(F[N])

