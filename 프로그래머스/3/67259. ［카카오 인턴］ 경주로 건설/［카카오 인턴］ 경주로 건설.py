from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    directions = [(1,0), (-1, 0), (0,-1), (0,1)]
    cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    
    queue = deque()
    
    for d in [0,3]: # 첫 시작은 항상 오른쪽, 아래로 시작
        cost[0][0][d] = 0
        queue.append((0, 0, d, 0))
        
    while queue:
        x, y, dir, cur_cost = queue.popleft()
        
        for new_dir, (dx, dy) in enumerate(directions):
            ax = x + dx
            ay = y + dy
            if 0 <= ax < N and 0 <= ay < N and board[ax][ay] == 0:
                if dir == new_dir:
                    new_cost = cur_cost + 100
                else:
                    new_cost = cur_cost + 600
                if new_cost < cost[ax][ay][new_dir]:
                    cost[ax][ay][new_dir] = new_cost
                    queue.append((ax,ay,new_dir,new_cost))
                    

            
        
    
    return min(cost[N-1][N-1])