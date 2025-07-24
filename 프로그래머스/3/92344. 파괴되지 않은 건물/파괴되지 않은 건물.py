def solution(board, skill):
    # board : 건물의 내구도
    # skill : 적의 공격 혹은 아군의 회복 스킬
    
    # skill -> type, r1, c1, r2, c2, degree
    # type 1 -> 공격, type 2 -> 회복
    
    n = len(board)
    m = len(board[0])
    effect = [[0] * (m+1) for _ in range(n+1)]
    
    for s in skill:
        type_, r1, c1, r2, c2, degree = s
        if type_ == 1:
            degree = -degree
        
        effect[r1][c1] += degree
        effect[r1][c2+1] -= degree
        effect[r2+1][c1] -= degree
        effect[r2+1][c2+1] += degree
    
    
    for i in range(n):
        for j in range(1, m):
            effect[i][j] += effect[i][j-1]
    
    for i in range(1,n):
        for j in range(m):
            effect[i][j] += effect[i-1][j]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += effect[i][j]
            if board[i][j] > 0:
                answer += 1
    
    
    
    
        
    
    
    return answer