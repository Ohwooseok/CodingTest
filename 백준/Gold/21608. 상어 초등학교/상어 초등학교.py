n = int(input())

dic = {}

seat = []

for i in range(n):
    seat.append([])
    for j in range(n):
        seat[i].append(0)


for _ in range(n * n):
    data = list(map(int, input().split()))
    key = data[0]
    value = data[1:]
    dic[key] = value


def blank(s, n): # 비어있는 칸 확인하는 함수
    real = []

    for i in range(n):
        for j in range(n):
            if s[i][j] == 0:
                real.append([i,j])

    return real


# 1 단계에서 좋아하는 학생이 인접한 칸에 가장 많은 칸의 좌표들을 저장해서 리턴
def chapter1(s, d, n, r, k): # seat, dic, n, real, key
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    rd = {}

    for a in r:
        x = a[0]
        y = a[1]
        rd[(x,y)] = 0

        for dd in range(4):
            dx = x + nx[dd]
            dy = y + ny[dd]
            if 0 <= dx < n and 0 <= dy < n:
                if s[dx][dy] in d[k]: # x , y 인접한 칸에 좋아하는 학생이 있는 경우
                    rd[(x,y)] += 1

    maxi = max(rd.values())
    result = []
    for kk in rd.keys():
        if rd[kk] == maxi:
            result.append(kk)

    return result


def chapter2(r, s): # result, seat
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    rd = {}

    for a in r:
        x = a[0]
        y = a[1]
        rd[(x,y)] = 0

        for dd in range(4):
            dx = x + nx[dd]
            dy = y + ny[dd]
            if 0 <= dx < n and 0 <= dy < n:
                if s[dx][dy] == 0: # x , y 인접한 칸에 좋아하는 학생이 있는 경우
                    rd[(x,y)] += 1

    maxi = max(rd.values())
    result = []
    for kk in rd.keys():
        if rd[kk] == maxi:
            result.append(kk)

    return result


for k in dic.keys():
    rr = blank(seat, n)

    one = chapter1(seat, dic, n, rr, k)
    if len(one) > 1: # 1을 만족하는 칸이 여러개이면
        two = chapter2(one, seat)
        if len(two) > 1: # 2를 만족하는 칸이 여러개이면
            best_pos = min(two, key=lambda x: (x[0], x[1]))
            x, y = best_pos
            seat[x][y] = k
        else:
            x, y = two[0]
            seat[x][y] = k
            continue
    else: # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함
        x, y = one[0]
        seat[x][y] = k
        continue

r = 0
for i in range(n):
    for j in range(n):
        hola = 0
        nx = [-1, 1, 0, 0]
        ny = [0, 0, -1, 1]
        for dd in range(4):
            dx = i + nx[dd]
            dy = j + ny[dd]
            if 0 <= dx < n and 0 <= dy < n:
                if seat[dx][dy] in dic[seat[i][j]]:
                    hola += 1
        if hola == 0:
            r += 0
        elif hola == 1:
            r += 1
        elif hola == 2:
            r += 10
        elif hola == 3:
            r += 100
        elif hola == 4:
            r += 1000

print(r)