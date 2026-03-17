import sys
import io
import math
from collections import defaultdict
from collections import deque
from collections import Counter
from itertools import combinations
import copy



n, m = map(int, input().split())

dod = deque()
sud = deque()

for _ in range(n):
    d, s = map(int, input().split())
    dod.append(d)
    sud.append(s)

dog = deque()
sug = deque()

for turn in range(m):
    if turn % 2 == 0:  # 도도 차례
        dog.append(dod.pop())
        if not dod:
            print("su")
            sys.exit()
    else:  # 수연 차례
        sug.append(sud.pop())
        if not sud:
            print("do")
            sys.exit()

    # 도도 종
    if (dog and dog[-1] == 5) or (sug and sug[-1] == 5):
        while sug:
            dod.appendleft(sug.popleft())
        while dog:
            dod.appendleft(dog.popleft())

    # 수연 종
    elif dog and sug and dog[-1] + sug[-1] == 5:
        while dog:
            sud.appendleft(dog.popleft())
        while sug:
            sud.appendleft(sug.popleft())

if len(dod) > len(sud):
    print("do")
elif len(dod) < len(sud):
    print("su")
else:
    print("dosu") 