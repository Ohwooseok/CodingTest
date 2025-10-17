import sys
import io
from collections import Counter


n = int(input())

word = []

for _ in range(n):
    word.append(input())

first = word[0]
first_c = Counter(first)


result = 0

for w in word[1:]:
    compare = Counter(w)

    diff = 0
    for ch in (first_c.keys()) | (compare.keys()):
        diff += abs(first_c[ch] - compare[ch])

    if diff == 0 or diff == 1 or (diff == 2 and len(first) == len(w)):
        result += 1

print(result)