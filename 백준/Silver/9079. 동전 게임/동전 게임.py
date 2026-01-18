import sys
from collections import deque

flip = [
    0b111000000,  # row1
    0b000111000,  # row2
    0b000000111,  # row3
    0b100100100,  # col1
    0b010010010,  # col2
    0b001001001,  # col3
    0b100010001,  # diag1
    0b001010100   # diag2
]

t = int(sys.stdin.readline())

for _ in range(t):
    board = []
    for _ in range(3):
        board += sys.stdin.readline().split()

    start = 0
    for i in range(9):
        if board[i] == 'T':
            start |= 1 << i

    dp = [-1] * 512

    q = deque()
    q.append(start)
    dp[start] = 0

    while q:
        cur = q.popleft()

        for f in flip:
            nxt = cur ^ f

            if dp[nxt] == -1:
                dp[nxt] = dp[cur] + 1
                q.append(nxt)

    res = dp[0]
    if dp[511] != -1:
        if res == -1:
            res = dp[511]
        else:
            res = min(res, dp[511])

    print(res)
