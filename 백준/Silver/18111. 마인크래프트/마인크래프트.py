import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

# 높이 카운트 배열
cnt = [0] * 257
for _ in range(N):
    for h in map(int, input().split()):
        cnt[h] += 1

min_h = next(i for i in range(257) if cnt[i] > 0)
max_h = max(i for i in range(257) if cnt[i] > 0)

best_time = float("inf")
best_height = -1

for h in range(min_h, max_h + 1):
    remove, add = 0, 0

    for height in range(min_h, max_h + 1):
        if cnt[height] == 0:
            continue
        diff = height - h
        if diff > 0:  # 블록 제거
            remove += diff * cnt[height]
        else:  # 블록 추가
            add -= diff * cnt[height]

    if remove + B >= add:
        time = remove * 2 + add
        if time < best_time or (time == best_time and h > best_height):
            best_time, best_height = time, h

print(best_time, best_height)
