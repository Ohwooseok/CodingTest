import math
def solution(n, stations, w):
    answer = 0

    position = 1
    cover = 2 * w + 1
    
    for station in stations:
        
        # 기존 기지국으로 커버가 안되는 아파트의 시작
        now = station - w
        
        if position < now:
            # 기존 기지국으로 커버가 안되는 아파트의 개수
            gap = now - position
            # gap을 커버할 수 있는 기지국 개수를 추가
            answer += math.ceil(gap / cover)
        
        position = station + w + 1
        
    
    # 기존 기지국으로도 커버가 안되는 범위가 오른쪽에 있을 때
    if position <= n:
        gap = n - position + 1
        answer += math.ceil(gap/cover)

    return answer