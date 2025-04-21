n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]


mini = 99999999999

for i in range(1, 1 << n):
    s = 1
    b = 0
    for j in range(n):
        if i & (1 << j):
            ss = ingredients[j][0]
            bb = ingredients[j][1]
            s *= ss
            b += bb

    mini = min(mini, abs(s - b))

print(mini)