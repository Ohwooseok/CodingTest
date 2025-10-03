import sys
import io


n = int(input())
board = [list(input()) for _ in range(n)]


def check():
    result = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
               cnt += 1
               result = max(result, cnt)
            else:
                cnt = 1

    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

    return result

answer = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i + 1 < n and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(answer)