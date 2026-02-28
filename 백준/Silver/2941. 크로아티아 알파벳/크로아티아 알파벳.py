import sys
import io
from collections import defaultdict



s = input().strip()


abc = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for a in abc:
    s = s.replace(a,"*")

print(len(s))