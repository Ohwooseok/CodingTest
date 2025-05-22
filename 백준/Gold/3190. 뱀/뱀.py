from collections import deque

N = int(input())

# 보드 상태 초기화
where = []
snake = deque([])  # 뱀의 위치들 저장
for i in range(N):
    where.append([])
    for _ in range(N):
        where[i].append(0)

# 사과 위치 입력
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    where[i-1][j-1] = 1  # 보드 위치는 0-indexed

# 방향 전환 정보 입력 (deque로 저장)
L = int(input())
t = deque()
for _ in range(L):
    X, C = input().split()
    t.append((int(X), C))

# 뱀 초기 상태
snake.append((0, 0))
a, b = 0, 0  # 머리 좌표
d = 0  # 처음 방향: 오른쪽
time = 0

# 방향: 동, 남, 서, 북
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while True:
    # 머리를 다음 칸에 위치시킴
    a += direct[d][0]
    b += direct[d][1]
    time += 1

    # 벽 또는 자기 몸에 부딪혔는지 확인
    if not (0 <= a < N and 0 <= b < N):
        break
    if (a, b) in snake:
        break

    snake.append((a, b))

    if where[a][b] == 1:  # 사과가 있다면
        where[a][b] = 0
    else:
        snake.popleft()  # 사과가 없으면 꼬리 제거

    # 방향 전환
    if t and time == t[0][0]:
        if t[0][1] == 'D':
            d = (d + 1) % 4
        else:  # 'L'
            d = (d - 1) % 4
        t.popleft()

print(time)