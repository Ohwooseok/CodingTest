import sys

# 입력
n = int(input())                           # 수의 개수 N
nums = list(map(int, input().split()))     # 수열 A1 ~ AN
plus, minus, mul, div = map(int, input().split())  # 연산자 개수

# 결과 초기값 (제한 조건 고려하여 설정)
max_val = -1_000_000_000
min_val = 1_000_000_000

def dfs(idx, current, p, m, mul_, d):
    global max_val, min_val
    if idx == n:
        # 마지막 수까지 계산했을 때
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return

    # 각각의 연산자가 남아 있다면 해당 연산으로 다음 수와 계산
    if p > 0:
        dfs(idx + 1, current + nums[idx], p - 1, m, mul_, d)
    if m > 0:
        dfs(idx + 1, current - nums[idx], p, m - 1, mul_, d)
    if mul_ > 0:
        dfs(idx + 1, current * nums[idx], p, m, mul_ - 1, d)
    if d > 0:
        if current < 0:
            # 음수 나눗셈 C++14 방식: 음수 → 양수 → 몫 → 다시 음수
            dfs(idx + 1, -(-current // nums[idx]), p, m, mul_, d - 1)
        else:
            dfs(idx + 1, current // nums[idx], p, m, mul_, d - 1)

# 처음 수부터 시작, index = 1부터 연산 시작
dfs(1, nums[0], plus, minus, mul, div)

# 결과 출력
print(max_val)
print(min_val)
