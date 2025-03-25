from collections import Counter

def solution(str1, str2):
    answer = 0
    sstr1 = []
    sstr2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        a = ""
        if str1[i].isalpha():
            a += str1[i]
        else:
            continue
        if str1[i+1].isalpha():
            a += str1[i+1]
        else:
            continue
        
        sstr1.append(a)
    
    for i in range(len(str2)-1):
        a = ""
        if str2[i].isalpha():
            a += str2[i]
        else:
            continue
        if str2[i+1].isalpha():
            a += str2[i+1]
        else:
            continue
        
        sstr2.append(a)
    
    counter1 = Counter(sstr1)
    counter2 = Counter(sstr2)
    
    same = counter1 | counter2
    diff = counter1 & counter2
    
    samec = sum(same.values())
    diffc = sum(diff.values())
    
    if samec == 0 and diffc == 0:
        return 65536
    else:
        return int((diffc / samec) * 65536)
    
    
    return answer