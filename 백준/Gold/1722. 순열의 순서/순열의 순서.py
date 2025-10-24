import sys
import io
from itertools import permutations
import math
import copy


n = int(input())

numbers = [i for i in range(1, n + 1)]

data = list(map(int, input().split()))

if data[0] == 1:
    k = data[1]
    k -= 1
    result = []

    for i in range(n, 0, -1):
        fact = math.factorial(i-1)
        idx = k // fact
        result.append(numbers[idx])
        numbers.pop(idx)
        k %= fact

    print(*result)
else:
    seq = data[1:]
    k = 1

    for i in range(n):
        smaller = 0
        for num in numbers:
            if num < seq[i]:
                smaller += 1
            else:
                break
        k += smaller * math.factorial(n-i-1)

        numbers.remove(seq[i])

    print(k)


