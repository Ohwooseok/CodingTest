def is_match(user, ban):
    if len(user) != len(ban):
        return False
    for u, b in zip(user, ban):
        if b == '*':
            continue
        if u != b:
            return False
    return True

def solution(user_id, banned_id):
    from itertools import permutations
    
    possible_cases = set()
    
    for case in permutations(user_id, len(banned_id)):
        # 각 banned_id와 user_id를 하나씩 비교
        if all(is_match(u, b) for u, b in zip(case, banned_id)):
            # set으로 만들어 순서 상관없이 고유하게 저장
            possible_cases.add(frozenset(case))
    
    return len(possible_cases)
