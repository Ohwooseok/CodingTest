import sys
sys.setrecursionlimit(10**7)  # 충분히 큰 수로 설정

def solution(n, m, x, y, r, c, k):
    from collections import deque

    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    
    def is_possible(x, y, dist):
        remain = abs(x - r) + abs(y - c)
        return remain <= (k - dist) and (k - dist - remain) % 2 == 0

    answer = []

    def dfs(x, y, path, depth):
        if answer:
            return  # 이미 답을 찾았으면 탐색 종료
        if depth == k:
            if (x, y) == (r, c):
                answer.append(path)
            return

        for d, dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= m:
                if is_possible(nx, ny, depth + 1):
                    dfs(nx, ny, path + d, depth + 1)

    if not is_possible(x, y, 0):
        return "impossible"

    dfs(x, y, "", 0)

    return answer[0] if answer else "impossible"
