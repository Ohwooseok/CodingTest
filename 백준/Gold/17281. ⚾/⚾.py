import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
main = [list(map(int, input().split())) for _ in range(n)]

players = [2,3,4,5,6,7,8,9]

def simul(rot):
    idx = 0
    score = 0

    for inning in main:
        out = 0
        b1 = b2 = b3 = 0
        while out < 3:
            res = inning[rot[idx] - 1]

            if res == 0:
                out += 1
            elif res == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif res == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif res == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1 = b2 = b3 = 0

            idx = (idx + 1) % 9

    return score

max_score = 0
for p in permutations(players):
    rot = list(p[:3]) + [1] + list(p[3:])
    max_score = max(max_score, simul(rot))

print(max_score)
