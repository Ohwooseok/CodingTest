def solution(n, k, cmd):
    
    # "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
    # "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
    # "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
    # "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
    
    # 행의 개수 n, 행의 위치를 나타내는 정수 k, 
    
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    
    next[n-1] = -1
    
    deleted = []
    
    curr = k
    
    alive = ['O'] * n
    
    for c in cmd:
        if c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                curr = prev[curr]
        
        elif c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                curr = next[curr]
        
        elif c[0] == 'C':
            deleted.append((curr, prev[curr], next[curr]))
            alive[curr] = 'X'
        
            if prev[curr] != -1:
                next[prev[curr]] = next[curr]

            if next[curr] != -1:
                prev[next[curr]] = prev[curr]


            curr = next[curr] if next[curr] != -1 else prev[curr]
        
        elif c[0] == 'Z':
            now, p, n_ = deleted.pop()
            alive[now] = 'O'

            if p != -1:
                next[p] = now
            if n_ != -1:
                prev[n_] = now

        
    return ''.join(alive)