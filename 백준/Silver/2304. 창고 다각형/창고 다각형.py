import sys
import io


n = int(input())
ki = []

for i in range(n):
    ki.append(list(map(int, input().split())))

sort_ki = sorted(ki, key=lambda x: x[0])

max_ki = float('-inf')
for s in sort_ki:
    if max_ki < s[1]:
        max_ki = s[1]

left_max_x = 0
gangx, gangh = sort_ki[0]
nurbi = 0
for s in sort_ki:
    x, h = s # 현재 좌표와 높이

    if h == max_ki:
        nurbi += abs((x-gangx)) * gangh
        left_max_x = x
        break

    if gangh < h: # 면적 계산 및 좌표 및 높이 갱신 필요
        nurbi += abs((x - gangx)) * gangh
        gangx = x
        gangh = h
    else:
        continue


ggangx, ggangh = sort_ki[-1]
right_max_x = 0

for i in range(len(sort_ki)-1, -1, -1):
    x, h = sort_ki[i]

    if h == max_ki:
        nurbi += ((ggangx - x) * ggangh)
        right_max_x = x
        break

    if ggangh < h:
        nurbi += (ggangx - x) * ggangh
        ggangx = x
        ggangh = h
    else:
        continue

nurbi += max_ki * (right_max_x - left_max_x +1)
print(nurbi)