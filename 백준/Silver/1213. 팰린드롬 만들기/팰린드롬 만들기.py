import sys
import io
from collections import defaultdict
from collections import deque



# 길이가 짝수 -> 모든 문자의 개수가 짝수
# 길이가 홀수 -> 딱 하나만 홀수, 나머지는 짝수

name = input()

count = [0] * 26

for c in name:
    count[ord(c) - ord("A")] += 1

odd = 0
mid = ""

for i in range(26):
    if count[i] % 2 == 1:
        odd += 1
        mid = chr(i + ord('A'))

if odd > 1:
    print("I'm Sorry Hansoo")
    exit()


left = []

for i in range(26):
    left.append(chr(i + ord('A')) * (count[i] // 2))
left = "".join(left)

right = left[::-1]

print(left + mid + right)