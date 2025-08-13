def solution(s):
    def transform(x):
        st = []
        cnt = 0
        for ch in x:
            st.append(ch)
            if ch == '0' and len(st) >= 3 and st[-3:] == ['1', '1', '0']:
                st.pop()
                st.pop()
                st.pop()
                cnt += 1
        
        rest = ''.join(st)
        
        p = rest.rfind('0')
        insert = '110' * cnt
        
        if p == -1:
            return insert + rest
        else:
            return rest[:p+1] + insert + rest[p+1:]
        

    
    return [transform(x) for x in s]