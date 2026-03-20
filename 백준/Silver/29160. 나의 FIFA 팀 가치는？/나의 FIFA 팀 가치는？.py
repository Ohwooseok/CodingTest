import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MAX_W = 100000

# position 1~11
freq = [[0] * (MAX_W + 1) for _ in range(12)]

for _ in range(N):
    p, w = map(int, input().split())
    freq[p][w] += 1

answer = 0

for pos in range(1, 12):
    # 이 포지션 선수 수가 0명이면 공석
    if sum(freq[pos]) == 0:
        continue

    # suffix_count[w] = 가치가 w 이상인 선수 수
    # suffix_sum[w]   = 가치가 w 이상인 선수 가치 합
    suffix_count = [0] * (MAX_W + 2)
    suffix_sum = [0] * (MAX_W + 2)

    for w in range(MAX_W, -1, -1):
        suffix_count[w] = suffix_count[w + 1] + freq[pos][w]
        suffix_sum[w] = suffix_sum[w + 1] + freq[pos][w] * w

    # 최댓값을 x 이하로 만들기 위해 필요한 감소 횟수
    def need(x):
        cnt = suffix_count[x + 1]   # x보다 큰 선수 수
        total = suffix_sum[x + 1]   # x보다 큰 선수 가치 합
        return total - cnt * x

    lo, hi = 0, MAX_W
    while lo <= hi:
        mid = (lo + hi) // 2
        if need(mid) <= K:
            hi = mid - 1
        else:
            lo = mid + 1

    # lo가 K년 12월 최종 선발 선수 가치
    answer += lo

print(answer)