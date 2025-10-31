import sys
import io
from itertools import permutations
import math
import copy


n, why = map(int, input().split())

digit = 1
start = 1

while 1:
    th_end = start * 10 - 1

    end = min(n, th_end)

    if end < start:
        print(-1)
        break

    conti_block = end - start + 1

    total_block = conti_block * digit

    if why > total_block:
        why -= total_block
        digit += 1
        start *= 10
        continue


    number_index = (why-1) // digit

    number = start + number_index

    char_index = (why-1) % digit

    print(str(number)[char_index])
    break