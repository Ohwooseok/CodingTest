from collections import defaultdict

def solution(gems):
    
    total_types = len(set(gems))  # 보석 종류 개수
    gem_counter = defaultdict(int)
    answer = [0, len(gems) - 1]
    start, end = 0, 0
    gem_counter[gems[0]] = 1
    
    while start <= end and end < len(gems):
        if len(gem_counter) == total_types:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            
            gem_counter[gems[start]] -= 1
            if gem_counter[gems[start]] == 0:
                del gem_counter[gems[start]]
            start += 1
        else:
            end += 1
            if end < len(gems):
                gem_counter[gems[end]] += 1
   
    return [answer[0] + 1, answer[1] + 1]
