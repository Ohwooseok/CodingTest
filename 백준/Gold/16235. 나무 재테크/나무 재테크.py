import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]  # 겨울 양분
nutr = [[5] * N for _ in range(N)]  # 현재 땅의 양분

# 각 칸별 {나이: 개수} 저장
trees = [[defaultdict(int) for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1][z] += 1

dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

for _ in range(K):
    new_trees = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
    dead = [[0]*N for _ in range(N)]  # 여름용

    # 🌱 봄 & 여름
    for r in range(N):
        for c in range(N):
            if not trees[r][c]:
                continue
            soil = nutr[r][c]
            temp = defaultdict(int)

            for age in sorted(trees[r][c].keys()):
                cnt = trees[r][c][age]
                if soil >= age * cnt:
                    # 전부 생존
                    soil -= age * cnt
                    temp[age + 1] += cnt
                else:
                    # 일부만 생존
                    alive = soil // age
                    if alive > 0:
                        temp[age + 1] += alive
                        soil -= alive * age
                    dead[r][c] += (cnt - alive) * (age // 2)
            nutr[r][c] = soil
            trees[r][c] = temp

    # ☀️ 여름 (양분 환원)
    for r in range(N):
        for c in range(N):
            nutr[r][c] += dead[r][c]

    # 🍂 가을 (번식)
    for r in range(N):
        for c in range(N):
            for age, cnt in trees[r][c].items():
                if age % 5 == 0:
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            new_trees[nr][nc][1] += cnt
            # 기존 나무들 유지
            for age, cnt in trees[r][c].items():
                new_trees[r][c][age] += cnt

    trees = new_trees

    # ❄️ 겨울 (양분 추가)
    for r in range(N):
        for c in range(N):
            nutr[r][c] += A[r][c]

# 🌳 결과 계산
ans = 0
for r in range(N):
    for c in range(N):
        ans += sum(trees[r][c].values())

print(ans)
