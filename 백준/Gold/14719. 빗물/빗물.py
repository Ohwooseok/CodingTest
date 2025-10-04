import sys
import io


n, m = map(int, input().split()) # 세로, 가로

block = list(map(int, input().split()))

max_index = block.index(max(block))

gij = block[0]

result = 0


for i in range(max_index):
    if block[i] <= gij:
        result += gij - block[i]
    else:
        gij = block[i]

gij = block[-1]
for j in range(len(block)-1, max_index, -1):
    if block[j] <= gij:
        result += gij - block[j]
    else:
        gij = block[j]

print(result)

