import heapq
import sys
import io
from collections import deque


s = input()
t = input()

while len(t) > len(s):
    if t[-1] == "A":
        t = t[:-1]
    else:
        t = t[:-1][::-1]

if t == s:
    print(1)
else:
    print(0)