import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0  # 모든 작업을 다 끝낼 수 있음

    # 최대 힙으로 만들기 (음수 부호 붙이기)
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)

    for _ in range(n):
        largest = heapq.heappop(max_heap)
        heapq.heappush(max_heap, largest + 1)  # +1 하는 이유: 음수로 저장했기 때문에

    return sum(work**2 for work in max_heap)