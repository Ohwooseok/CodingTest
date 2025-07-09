def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0

    def can_cross(x):
        skip = 0
        for stone in stones:
            if stone < x:
                skip += 1
                if skip >= k:
                    return False
            else:
                skip = 0
        return True

    while left <= right:
        mid = (left + right) // 2
        if can_cross(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
