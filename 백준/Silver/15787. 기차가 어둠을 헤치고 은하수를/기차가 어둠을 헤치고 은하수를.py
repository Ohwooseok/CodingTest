n, m = map(int, input().split())

train = [0] * (n+1)

for _ in range(m):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        _, i, x = cmd
        train[i] |= (1 << (x-1)) #  x번째 비트를 1로 설정 (예: x=3이면 0b00000100)

    elif cmd[0] == 2:
        _, i, x = cmd
        train[i] &= ~(1 << (x-1)) # x번째 비트만 0이고 나머진 1인 마스크

    elif cmd[0] == 3:
        _, i = cmd
        train[i] = (train[i] << 1) & ((1 << 20)-1)
        # train[i] << 1: 좌측으로 비트 쉬프트 → 뒤로 한 칸 이동
        # & ((1 << 20) - 1): 21번째 자리(초과 자리)는 자르기 → 0b111...111 (20비트 마스크)

    elif cmd[0] == 4:
        _, i = cmd
        train[i] >>= 1

print(len(set(train[1:])))