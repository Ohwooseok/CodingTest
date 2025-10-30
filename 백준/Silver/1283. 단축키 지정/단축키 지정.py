import sys
import io
from collections import defaultdict
import math
import copy


n = int(input())

r = set()

for _ in range(n):
    words = input().split()
    line = ' '.join(words)
    check = False

    start_idx = 0
    for word in words:
        idx = line.find(word, start_idx)
        if word[0].lower() not in r:
            r.add(word[0].lower())
            line = line[:idx] + "[" + line[idx] + "]" + line[idx+1:]
            check = True
            break
        else:
            continue
        start_idx = idx + len(word) + 1

    if not check:
        for idx, l in enumerate(line):
            if l != " " and l.lower() not in r:
                r.add(l.lower())
                line = line[:idx] + "[" + l + "]" + line[idx+1:]
                break
            else:
                continue
    print(line)
