import sys

S, E, Q = sys.stdin.readline().split()

def time_to_minute(t):
    h, m = map(int, t.split(":"))
    return 60 * h + m

makeS = time_to_minute(S)
makeE = time_to_minute(E)
makeQ = time_to_minute(Q)

enter = set()
exit_ok = set()

for line in sys.stdin:  # EOF까지 자동으로 읽음
    time_str, nickname = line.strip().split()
    t = time_to_minute(time_str)

    if t <= makeS:
        enter.add(nickname)

    if makeE <= t <= makeQ:
        if nickname in enter:
            exit_ok.add(nickname)

print(len(exit_ok))
