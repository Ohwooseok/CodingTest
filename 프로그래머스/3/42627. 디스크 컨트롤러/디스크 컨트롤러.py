import heapq

def solution(jobs):
    answer = 0
    sjobs = [(i,s,j) for i, (s,j) in enumerate(jobs)]
    
    sorted_jobs = sorted(sjobs, key = lambda x : x[1])
    time = 0
    total_timearound = 0
    job_index = 0
    job_count = len(sorted_jobs)
    heap = []
    
    while job_index < job_count or heap:
        while job_index < job_count and time >= sorted_jobs[job_index][1]:
            job_num, start, finish = sorted_jobs[job_index]
            heapq.heappush(heap, (finish, start, job_num))
            job_index += 1
        
        if heap:
            finish, start, job_num = heapq.heappop(heap)
            time += finish
            total_timearound += time - start
        else:
            time = sorted_jobs[job_index][1]
    
    
    
    
    return total_timearound // job_count