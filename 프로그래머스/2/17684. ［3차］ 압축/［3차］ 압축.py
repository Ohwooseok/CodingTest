def solution(msg):
    answer = []
    
    dic = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    
    i = 0
    while msg:
        
        while i < len(msg) and msg[:i+1] in dic:
            i += 1
        
        if i == len(msg):
            answer.append(dic.index(msg[:i+1])+1)
            break
        
        # dic에 없을 때
        answer.append(dic.index(msg[:i])+1) # answer에 색인 번호 추가
        dic.append(msg[:i+1]) # dic에 새로운 단어 추가
        msg = msg[i:] # msg에서 단어 제거
        i = 0 
        
        
    
    return answer