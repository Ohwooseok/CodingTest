import sys
import io
from collections import deque




n = int(input())


fn = [0] * (n+2)
fn[1] = 1
fn[2] = 1

for i in range(3, n+2):
    fn[i] = fn[i-1] + fn[i-2]

print(2 * (fn[n] + fn[n+1]))