n = int(input())
nlist = list(map(int, input().split()))

p, m, multi, divi = map(int, input().split())
max_man = -1_000_000_000
min_man = 1_000_000_000
def back(idx, current, plus, minus, multii, divii):
    global max_man, min_man
    if idx == n:
        max_man = max(max_man, current)
        min_man = min(min_man, current)
        return

    if plus > 0:
        back(idx+1, current+nlist[idx], plus-1, minus, multii, divii)
    if minus > 0:
        back(idx+1, current-nlist[idx], plus, minus-1, multii, divii)
    if multii > 0:
        back(idx+1, current*nlist[idx], plus, minus, multii-1, divii)
    if divii > 0:
        if current < 0:
            back(idx+1, -(abs(current) // nlist[idx]), plus, minus, multii, divii-1)
        else:
            back(idx+1, current // nlist[idx], plus, minus, multii, divii-1)


back(1, nlist[0], p, m, multi, divi)

print(max_man)
print(min_man)