def solution(coin, cards):
    n = len(cards)
    target = n + 1
    have = set(cards[:n//3])   # 처음 손패
    rest = cards[n//3:]        # 남은 덱
    pool = set()               # 앞으로 쓸 수 있는 카드 후보
    round_cnt = 1              # 첫 라운드

    # 두 장씩 덱에서 꺼내며 라운드 진행
    for i in range(0, len(rest), 2):
        # 새로 뽑은 카드 후보 풀에 추가
        pool.add(rest[i])
        if i + 1 < len(rest):
            pool.add(rest[i + 1])

        # 라운드를 통과할 수 있는지 체크
        success = False

        # (1) 손패끼리 바로 짝 맞출 수 있는가
        for x in list(have):
            if target - x in have:
                have.remove(x)
                have.remove(target - x)
                success = True
                break

        # (2) 손패 + 후보 (코인 1개)
        if not success and coin >= 1:
            for x in list(have):
                if target - x in pool:
                    have.remove(x)
                    pool.remove(target - x)
                    coin -= 1
                    success = True
                    break

        # (3) 후보끼리 (코인 2개)
        if not success and coin >= 2:
            for x in list(pool):
                if target - x in pool:
                    pool.remove(x)
                    pool.remove(target - x)
                    coin -= 2
                    success = True
                    break

        if success:
            round_cnt += 1
        else:
            break

    return round_cnt
