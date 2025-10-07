from itertools import combinations
from itertools import product
from bisect import bisect_left, bisect_right

def solution(dice):
    
    d = []
    for i in range(len(dice)):
        d.append(i)
    
    best_choice = None
    best_win = -1
    
    for adice in combinations(d, int(len(dice)/2)):
        adice = list(adice)
        bdice = []
        for dd in d:
            if dd not in adice:
                bdice.append(dd)
        # adice = [0,1]
        # bdice = [2,3]
        alla = []
        for a in adice:
            alla.append(dice[a])
        allb = []
        for b in bdice:
            allb.append(dice[b])
            
        ap = [sum(x) for x in product(*alla)]
        bp = [sum(x) for x in product(*allb)]
            
        ap.sort()
        bp.sort()

        win = 0
        tie = 0
        
        for a in ap:
            lt = bisect_left(bp, a)
            win += lt
        
        if win > best_win:
            best_win = win
            best_choice = adice
        
    
    return [i + 1 for i in best_choice]  # → [1, 4]
