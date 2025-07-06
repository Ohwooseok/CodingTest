def solution(genres, plays):
    answer = []
    
    # 일단 장르별로 재생된 횟수를 저장
    dic1 = {}
    # 장르별로 재생 횟수 노래 저장
    dic2 = {}
    
    for i in range(len(genres)):
        if genres[i] not in dic1:
            dic1[genres[i]] = plays[i]
        else:
            dic1[genres[i]] += plays[i]
        
        if genres[i] in dic2:
            dic2[genres[i]].append((i, plays[i]))
        else:
            dic2[genres[i]] = [(i, plays[i])]
    
    # dic1의 많이 재생된 장르를 기준으로 정렬
    sorted_genres = sorted(dic1, key = lambda x: dic1[x], reverse=True)
    
    for genre in sorted_genres:
        # 많이 재생된 노래를 정렬하고 재생 횟수가 같으면 고유번호가 낮은 노래를 정렬
        sorted_dic2 = sorted(dic2[genre], key = lambda x: (-x[1], x[0]))
        
        count = 0
        print(sorted_dic2)
        for s in sorted_dic2:
            answer.append(s[0])
            count += 1
            
            if count == 2:
                break
                
        
    
    
    return answer