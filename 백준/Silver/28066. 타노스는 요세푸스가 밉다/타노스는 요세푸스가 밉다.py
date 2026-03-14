import sys
import io
import math
from collections import defaultdict
from collections import deque
from collections import Counter



n, k = map(int, input().split(" "))

# k마리 제거
# 남아 있는 청설모가 K마리보다 작으면 첫 번째 청설모를 제외한 모든 청설모 제거
# 제거된 후 남아있는 청설모가 2마리 이상일 경우 첫번째 청설모의 오른쪽 청설모가
# 첫번째 청설모

q = deque([])

for i in range(1, n+1):
    q.append(i)




while True:
    if len(q) == 1:
        print(q[0])
        break

    if len(q) < k:
        a = q.popleft()   # 첫 번째 청설모
        q.clear()         # 나머지 전부 제거
        q.append(a)       # 첫 번째만 다시 넣기

    else:
        a = q.popleft()   # 첫 번째 청설모는 생존

        for _ in range(k - 1):
            q.popleft()   # 2번째 ~ K번째 제거

        q.appendleft(a)   # 생존한 첫 번째를 맨 앞에 복원

    if len(q) >= 2:
        a = q.popleft()
        q.append(a)       # 첫 번째의 오른쪽 청설모를 다음 첫 번째로 만들기