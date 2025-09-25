def solution(n):
    answer = []
    
    board = [[0] * n for _ in range(n)]
    
    directions = [(1,0), (0,1), (-1,-1)]
    
    d = 0
    x, y = 0, 0
    
    last = n * (n + 1) // 2
    
    for l in range(1, last+1):
        
        board[x][y] = l
        
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] != 0:
            d = (d+1) % 3
            nx = x + directions[d][0]
            ny = y + directions[d][1]
        
        x, y = nx, ny
    
    for i in range(n):
        answer.extend(board[i][:i+1])
    
    return answer