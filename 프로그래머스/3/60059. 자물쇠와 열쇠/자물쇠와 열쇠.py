def rotate_90(key):
    M = len(key)
    
    rotated_key = []
    for i in range(M):
        new_rotate = []
        for j in range(M):
            new_rotate.append(key[M-j-1][i])
        
        rotated_key.append(new_rotate)
    
    return rotated_key

def check(new_lock, N, M):
    for i in range(N):
        for j in range(N):
            if new_lock[i+M][j+M] != 1:
                return False
    
    return True

def solution(key, lock):
    
    M = len(key)
    N = len(lock)
    
    expand_size = N + 2 * M
    expand_lock = []
    
    # 자물쇠 배열 초기화
    for _ in range(expand_size):
        row = [0] * expand_size
        expand_lock.append(row)
    
    for i in range(N):
        for j in range(N):
            expand_lock[i + M][j + M] = lock[i][j]
            
    
    for _ in range(4):
        key = rotate_90(key)
        
        for x in range(1 + N + M -1):
            for y in range(1 + N + M -1):
                temp_lock = []
                for row in expand_lock:
                    copied_row = row[:]
                    temp_lock.append(copied_row)
            
                for i in range(M):
                    for j in range(M):
                        temp_lock[x+i][y+j] += key[i][j]
                
                if check(temp_lock, N, M):
                    return True
    return False
    
    