import sys
import io
from collections import defaultdict
from collections import deque




n = int(input())
questions = []

for _ in range(n):
    num, strike, ball = map(int, input().split())
    questions.append((str(num), strike, ball))

answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):

            if a == b or b == c or c == a:
                continue

            candidate = str(a) + str(b) + str(c)

            possible = True

            for num, str_c, ball_c in questions:
                strike = 0
                ball = 0

                for i in range(3):
                    if candidate[i] == num[i]:
                        strike += 1
                    elif candidate[i] in num:
                        ball += 1
                if strike != str_c or ball != ball_c:
                    possible = False
                    break

            if possible:
                answer += 1

print(answer)