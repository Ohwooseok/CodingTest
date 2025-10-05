import sys
import io
from collections import deque


n = int(input())
key = list(map(int, input().split()))

result = []

for i in range(n, 0, -1):
    result.insert(key[i-1], i)

print(*result)