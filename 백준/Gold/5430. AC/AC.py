import sys
import io
from collections import deque

t = int(input())

for _ in range(t):
    Fun = input().strip()
    N = int(input())
    arr = input().strip()

    if N == 0:
        rist = deque()
    else:
        rist = deque(map(int, arr.strip("[]").split(",")))

    reverse = False
    error_flag = False

    for f in Fun:
        if f == "R":
            reverse = not reverse
        else:  # D
            if not rist:
                print("error")
                error_flag = True
                break
            if reverse:
                rist.pop()   # 뒤에서 제거
            else:
                rist.popleft()  # 앞에서 제거

    if not error_flag:
        if reverse:
            rist.reverse()
        print("[" + ",".join(map(str, rist)) + "]")
