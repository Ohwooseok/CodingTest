def solution(record):
    logs = []
    uid_nick = {}
    answer = []
    
    for r in record:
        a = r.split()
        doing = a[0]
        Id = a[1]
        
        if doing in ("Enter", "Change"):
            nick = a[2]
            uid_nick[Id] = nick
        if doing in ("Enter", "Leave"):
            logs.append((Id, doing))
        
    
    for l in logs:
        doing = l[1]
        nick = uid_nick[l[0]]
        if doing == "Enter":
            answer.append(nick+"님이 들어왔습니다.")
        elif doing == "Leave":
            answer.append(nick+"님이 나갔습니다.")
           
    
    return answer