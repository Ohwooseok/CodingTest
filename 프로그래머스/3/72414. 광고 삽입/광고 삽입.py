def solution(play_time, adv_time, logs):
    
    def time_to_sec(t):
        h, m, s = map(int, t.split(":"))
        return h * 3600 + m * 60 + s
    
    def sec_to_time(sec):
        h = sec // 3600
        sec %= 3600
        m = sec // 60
        s = sec % 60
        return f"{h:02d}:{m:02d}:{s:02d}"
    
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    
    viewers = [0] * (play_sec + 2)
    
    for log in logs:
        start, end = log.split("-")
        start_sec = time_to_sec(start)
        end_sec = time_to_sec(end)
        viewers[start_sec] += 1
        viewers[end_sec] -= 1
    
    for i in range(1, play_sec+1):
        viewers[i] += viewers[i-1]
    
    
    prefix_sum = [0] * (play_sec + 2)
    for i in range(1, play_sec+1):
        prefix_sum[i] = prefix_sum[i-1] + viewers[i-1]
        
    

    
    max_time = 0
    start_time = 0
    for i in range(adv_sec, play_sec+1):
        total_time = prefix_sum[i] - prefix_sum[i - adv_sec]
        if total_time > max_time:
            max_time = total_time
            start_time = i - adv_sec
    
    return sec_to_time(start_time)

    
    
