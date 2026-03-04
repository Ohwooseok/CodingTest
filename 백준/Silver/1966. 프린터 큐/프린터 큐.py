import sys
import io
from collections import defaultdict
from collections import deque



n = int(input())



for _ in range(n):
    n, m = map(int, input().split()) # n = 문서의 개수, m = 순서 궁금한 문서

    imp = list(map(int, input().split()))

    q = deque([])

    for j in range(len(imp)):
        q.append((j, imp[j]))

    what = 1
    while q:
        max_value = max(x[1] for x in q)


        idx, cur = q.popleft()


        
        if cur < max_value: # 현재 문서보다 중요도가 높은 문서가 있음
            q.append((idx, cur)) # 가장 뒤에 재배치
        else:
            if m == idx: # 순서가 궁금한 문서일 때
                print(what)
            else:
                what += 1






