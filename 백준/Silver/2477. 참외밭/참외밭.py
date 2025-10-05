import sys
import io

n = int(input()) # 참외의 개수

ga = []
se = []
all = []

for i in range(6):
    dirr, length = map(int, input().split())
    all.append(length)
    if dirr in [1, 2]:
        ga.append(length)
    elif dirr in [3,4]:
        se.append(length)

max_ga = max(ga)
max_se = max(se)

max_ga_index = all.index(max_ga)
max_se_index = all.index(max_se)

sec_ga_index = (max_ga_index + 3) % 6
sec_se_index = (max_se_index + 3) % 6

print((max_ga * max_se - all[sec_ga_index] * all[sec_se_index]) * n)
