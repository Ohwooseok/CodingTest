import sys
import io
from collections import defaultdict
from collections import deque



direction = {
    "R": (0, 1), "L": (0, -1), "B": (-1, 0), "T": (1, 0),
    "RT": (1, 1), "LT": (1, -1), "RB": (-1, 1), "LB": (-1, -1)
}

king, stone, n = input().split()

kingx = ord(king[0]) - ord('A') + 1
kingy = int(king[1])

stonex = ord(stone[0]) - ord('A') + 1
stoney = int(stone[1])

for _ in range(int(n)):
    move = input().strip()
    dy, dx = direction[move]

    nkx = kingx + dx
    nky = kingy + dy

    # 킹이 체스판 밖이면 무시
    if not (1 <= nkx <= 8 and 1 <= nky <= 8):
        continue

    # 킹이 돌 위치로 이동하는 경우
    if nkx == stonex and nky == stoney:
        nsx = stonex + dx
        nsy = stoney + dy

        # 돌이 체스판 밖이면 무시
        if not (1 <= nsx <= 8 and 1 <= nsy <= 8):
            continue

        # 둘 다 이동
        kingx, kingy = nkx, nky
        stonex, stoney = nsx, nsy
    else:
        # 킹만 이동
        kingx, kingy = nkx, nky

print(chr(kingx + 64) + str(kingy))
print(chr(stonex + 64) + str(stoney))