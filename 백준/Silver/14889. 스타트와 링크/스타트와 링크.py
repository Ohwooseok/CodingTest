from itertools import combinations


n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]

people = list(range(n))
min_diff = 10000

for team in combinations(people, n//2):
    start_team = list(team)
    link_team = list(set(people) - set(start_team))

    start_score = 0
    link_score = 0

    for i in range(n//2):
        for j in range(n//2):
            if i == j:
                continue

            start_score += nlist[start_team[i]][start_team[j]]
            link_score += nlist[link_team[i]][link_team[j]]

    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)


print(min_diff)