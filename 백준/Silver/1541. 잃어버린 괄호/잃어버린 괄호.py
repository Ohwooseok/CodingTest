import sys
import io
from collections import deque


st = str(input())

firsts = st.split("-")
minus = 0 # - 해야될 총 값
total = 0
if len(firsts) == 1: # - 가 없는 경우
    s = firsts[0].split("+")
    for ss in s:
        total += int(ss)
else:
    for strr in firsts[1:]:
        if '+' in strr:
            s = strr.split("+")
            for ss in s:
                minus += int(ss)
        else:
            minus += int(strr)
    
    if "+" in firsts[0]:
        s = firsts[0].split("+")
        what = 0
        for ss in s:
            what += int(ss)
        
        total = what - minus
    else:
        total = int(firsts[0]) - minus

print(total)