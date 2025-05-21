
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

info = []

for _ in range(N):
    info.append(list(map(int, input().split())))

# 구름 이동 후 비가 내리고 물의 양이 1 증가하는 함수
def chapter123(g, inf, d, s): # groom, info, 방향, 몇칸
    direct = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
    dg = []
    for x, y in g:

        dx = (x + direct[d-1][0] * s) % len(inf)
        dy = (y + direct[d-1][1] * s) % len(inf)

        dg.append((dx,dy)) # 이동한 구름이 있는 좌표

    for x, y in dg:
        inf[x][y] += 1

    return inf, dg

# 대각선 방향에 물이 있는 바구니의 수 계산하는 함수
def digline(g, inf): # g : 물이 증가한 칸의 좌표
    direct = [(-1,-1), (-1,1), (1,1), (1,-1)]

    for x, y in g:
        much = 0
        for i in range(4):
            dx = x + direct[i][0]
            dy = y + direct[i][1]

            if 0 <= dx < len(inf) and 0 <= dy < len(inf):

                if inf[dx][dy] > 0:
                    much += 1

        inf[x][y] += much

    return inf

def chapter5(inf, dg): # dg : 3에서 구름이 있었던 좌표
    g = []
    for i in range(len(inf)):
        for j in range(len(inf)):
            if inf[i][j] >= 2 and (i,j) not in dg:
                inf[i][j] -= 2
                g.append((i,j))

    return inf, g

g = [(N-1,0), (N-1,1), (N-2,0), (N-2, 1)] # 비바라기 시전했을 때 첫번째 구름

for i in range(M):
    dd, ss = map(int, input().split())


    info, dg = chapter123(g, info, dd, ss)

    info = digline(dg, info)

    info, g = chapter5(info, dg)


result = 0

for i in range(N):
    for j in range(N):
        result += info[i][j]


print(result)
