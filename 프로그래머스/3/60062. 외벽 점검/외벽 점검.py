from itertools import permutations

def solution(n, weak, dist):
    
    # weak 배열을 2배로 확장해서 원형을 일자형으로 변환
    extended_weak = weak + [w + n for w in weak]
    
    long = len(weak)
    
    min_count = float('inf')
    
    for w in range(long):
        for friends in permutations(dist):
            count = 1
            position = extended_weak[w] + friends[count - 1]
            
            for a in range(w, w+long):
                if extended_weak[a] > position:
                    count += 1
                    if count > len(dist):
                        break
                    position = extended_weak[a] + friends[count - 1]
                    
            
            min_count = min(min_count, count)
    
    return min_count if min_count <= len(dist) else -1