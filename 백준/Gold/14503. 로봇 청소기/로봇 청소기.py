n, m = map(int, input().split())

sx, sy, sdi = map(int, input().split())

where = []

for _ in range(n):
    where.append(list(map(int, input().split())))

check = [ [False] * m for _ in range(n)]

result = 0
# 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]  # row 변화
dy = [0, 1, 0, -1]  # col 변화

def check_direct(x):
    new_dir = (x + 3) % 4  # 반시계 방향 90도 회전
    return [new_dir, (dx[new_dir], dy[new_dir])]



while 1:
    isit = False
    hmm = True
    direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서
    # 현재 칸이 청소되지 않은 경우, 현재 칸을 청소
    if where[sx][sy] == 0 and not check[sx][sy]:
        check[sx][sy] = True
        result += 1

    for ax, ay in direct:
        nx = ax + sx
        ny = ay + sy
        # 현재 칸의 주변 4칸 중 청소 되지 않은 빈 칸이 있을 경우
        if 0 <= nx < n and 0 <= ny < m:
            if where[nx][ny] == 0 and not check[nx][ny]:
                isit = True
                break

    if isit: # 청소 되지 않은 빈칸이 있을 경우
        while 1:
            what = check_direct(sdi)
            sdi = what[0] # 방향을 반시계 방향으로 회전
            nx = what[1][0] + sx
            ny = what[1][1] + sy

            if 0 <= nx < n and 0 <= ny < m:
                # 바라보는 방향을 기준으로 앞쪽 칸이 청소 되지 않은 빈 칸인 경우
                if where[nx][ny] == 0 and not check[nx][ny]:
                    # 한 칸 전진
                    sx = nx
                    sy = ny
                    break
    else: # 청소되지 않은 빈 칸이 없는 경우
        bx = sx - dx[sdi]  # 180도 반대방향
        by = sy - dy[sdi]

        if 0 <= bx < n and 0 <= by < m:
            if where[bx][by] == 1:  # 벽이라면 종료
                break
            else:
                sx, sy = bx, by  # 후진
                continue



print(result)