import sys
import io
from collections import defaultdict
import math
import copy


n = int(input())
total = int(input())
what = list(map(int, input().split()))

page = defaultdict(list)



for w in what:
    if w in page:
        page[w][0] += 1
    else: # 딕셔너리에 없는 값
        if len(page.keys()) < n: # 사진틀 개수보다 작아
            page[w].append(1)
            page[w].append(0)
        else:
            sort_page = sorted(page.items(), key = lambda x: (x[1][0], -x[1][1]))
            sort_page.pop(0)
            sort_page.append((w, [1,0]))
            page = dict(sort_page)
    
    for value in page.values():
        value[1] += 1

sort_result = sorted(page.items(), key = lambda x: x[0])
result = []
for s in sort_result:
    result.append(s[0])

print(*result)


