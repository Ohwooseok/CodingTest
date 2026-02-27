import sys
import io
from collections import defaultdict




n = int(input())

count = 0
for i in range(n):
    str1 = str(input())
    check = defaultdict(bool)
    cur = str1[0]
    is_group = True

    for s in str1:

        if not cur == s: # 그 전 단어와 다를 때
            check[cur] = True

            if check[s]:
                is_group = False
                break

            cur = s

    if is_group:
        count += 1


print(count)
