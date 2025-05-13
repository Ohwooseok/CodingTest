total = []

for _ in range(4):
    total.append([int(f) for f in input().strip()])

k = int(input())


# 각 톱니바퀴의 3번째 확인해서 어떻게 회전하는지 확인
# 회전 한 후에 톱니바퀴의 N, S 순서 재정렬 (i+1) % n 이런 느낌으로
# 회전 시킨 이후로 12시방향의 극에 따라 점수 다르게 계산

result = 0

for _ in range(k):
    what, where = map(int, input().split())
    what -= 1

    dirs = [0] * 4
    dirs[what] = where

    # 오른쪽 전파
    for i in range(what, 3):
        if total[i][2] != total[i+1][6]:
            dirs[i+1] = -dirs[i]
        else:
            break

    # 왼쪽 전파
    for i in range(what, 0, -1):
        if total[i][6] != total[i-1][2]:
            dirs[i-1] = -dirs[i]
        else:
            break

    # 회전
    for i in range(4):
        if dirs[i] == 1:  # 시계
            total[i] = [total[i][-1]] + total[i][:-1]
        elif dirs[i] == -1:  # 반시계
            total[i] = total[i][1:] + [total[i][0]]

for i in range(len(total)):
    if total[i][0] == 0: # 12시 방향이 N극이면
        continue
    else:
        result += 2 ** i

print(result)