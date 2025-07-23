from collections import defaultdict

def solution(scores):
    no = set()  # 리스트 → set
    yes = []

    wanho = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    dic = defaultdict(list)

    max_man = 0
    for s in scores:
        if s[1] < max_man:
            if s == wanho:
                return -1
            no.add(tuple(s))  # 리스트를 튜플로 변환해 저장
        else:
            max_man = max(max_man, s[1])

    for s in scores:
        if tuple(s) not in no:  # set에서는 튜플로 비교
            yes.append(tuple(s))  # 이후 딕셔너리에 쓸 거니까 튜플로 저장

    for y in yes:
        dic[sum(y)].append(y)

    sorted_dict = dict(sorted(dic.items(), reverse=True))

    answer = 1
    for value in sorted_dict.values():
        if tuple(wanho) in value:  # 완호도 튜플로 비교
            return answer
        answer += len(value)

    return answer
