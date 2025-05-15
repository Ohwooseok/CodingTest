from itertools import combinations
n, m = map(int,input().split())
where = []

for _ in range(n):
    where.append(list(map(int, input().split())))
house = []
chicken = []


# 치킨집과 집의 좌표 정보 리스트에 저장
for i in range(n):
    for j in range(n):
        if where[i][j] == 1:
            house.append((i,j))
        elif where[i][j] == 2:
            chicken.append((i,j))



def distance(i,j,k,l):
    return abs(i-k) + abs(j-l)

def chicken_distance(h, c): # 정해진 집과 치킨집에 따라서 각각의 치킨 거리를 구하는 함수

    result = 0
    for i,j in h:
        mini = 1_000_000_000
        for k,l in c:
            mini = min(mini, distance(i,j,k,l))

        result += mini

    return result


mini = 1_000_000_000
for p in combinations(chicken, m):
    mini = min(mini, chicken_distance(house, p))

print(mini)