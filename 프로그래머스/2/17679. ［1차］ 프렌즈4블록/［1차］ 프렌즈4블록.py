def solution(m, n, board):
    # 문자열 리스트를 2차원 리스트로 변환
    board = [list(row) for row in board]
    total_removed = 0

    while True:
        remove = set()

        # 2x2 블록 탐색
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if block == ' ':
                    continue
                if block == board[i+1][j] and block == board[i][j+1] and block == board[i+1][j+1]:
                    remove.update({(i,j), (i+1,j), (i,j+1), (i+1,j+1)})

        # 제거할 게 없으면 종료
        if not remove:
            break

        # 블록 지우기
        for i, j in remove:
            board[i][j] = ' '
        total_removed += len(remove)

        # 블록 아래로 떨어뜨리기
        for j in range(n):
            empty = []
            for i in reversed(range(m)):
                if board[i][j] == ' ':
                    empty.append(i)
                elif empty:
                    empty_i = empty.pop(0)
                    board[empty_i][j] = board[i][j]
                    board[i][j] = ' '
                    empty.append(i)

    return total_removed
