import sys
import io
from collections import Counter
import copy
import math


n = int(input())
num_n = list(map(int, input().split()))

m = int(input())
num_m = list(map(int, input().split()))

total_n = 1
total_m = 1

for numn in num_n:
    total_n *= numn

for numm in num_m:
    total_m *= numm

result = math.gcd(total_n, total_m)

if len(str(result)) > 9:
    result = str(result)
    print(result[len(result) - 9:])
else:
    print(result)


