from collections import deque
n, k = map(int, input().split())
dur = list(map(int, input().split()))
rob = [0 for _ in range(2*n)] # 벨트 개수에 따라 로봇 들어가있음 0 은 없다는 뜻

dur_belt = deque(dur)
rob_belt = deque(rob)

# 한 칸 회전하는 함수 -> dur도 회전해야되고


def robot_rotate(dur, rob): # sta는 벨트에 올라간 순서대로 저장한 스택
    for i in range(n - 2, -1, -1):  # N-2 ~ 0 까지 (내리는 위치 직전까지만)
        if rob[i] != 0 and rob[i + 1] == 0 and dur[i + 1] > 0:
            rob[i + 1] = rob[i]
            rob[i] = 0
            dur[i + 1] -= 1
    rob[n - 1] = 0  # 내리는 위치 로봇 제거
    return dur, rob


check = 1

while 1:

    # 1 단계 : 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    dur_belt.rotate(1)
    rob_belt.rotate(1)
    rob_belt[n-1] = 0



    # 2 단계
    dur_belt, rob_belt = robot_rotate(dur_belt, rob_belt)


    # 3 단계
    if dur_belt[0] > 0 and rob_belt[0] == 0:
        rob_belt[0] = 1
        dur_belt[0] -= 1


    # 4 단계
    if dur_belt.count(0) >= k:
        break
    check += 1


print(check)