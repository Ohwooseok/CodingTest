import sys
import io


N = int(input())

stack = []

for _ in range(N):
    stack.append(input().split())

final = input().split()

def Check(f):
    check = False
    for s in stack:
        if s and s[0] == f:
            del s[0]
            check = True
            break

    return check

final_check = True
for f in final:
    if Check(f):
        continue
    else:
        final_check = False
        break


if final_check:
    for s in stack:
        if not s:
            continue
        else:
            print("Impossible")
            sys.exit()
    print("Possible")
else:
    print("Impossible")