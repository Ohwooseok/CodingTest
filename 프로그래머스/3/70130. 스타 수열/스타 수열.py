from collections import Counter

def solution(a):
    if len(a) < 2:
        return 0

    count = Counter(a)
    answer = 0

    for v in count:
        if count[v] * 2 <= answer:
            continue

        i = 0
        pair = 0
        while i < len(a) - 1:
            if (a[i] == v or a[i+1] == v) and a[i] != a[i+1]:
                pair += 1
                i += 2
            else:
                i += 1
        answer = max(answer, pair * 2)

    return answer
