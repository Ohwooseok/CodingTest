def solution(n, t, m, p):
    ho = []
    
    def change(jin, number):
        if jin == 2:
            ch_list = list(bin(number)[2:])
        elif jin == 8:
            ch_list = list(oct(number)[2:])
        elif jin == 16:
            ch_list = list(hex(number)[2:].upper())
        else:
            c = '0123456789ABCDEF'
            res = ''
            if number == 0:
                return ['0']
            else:
                while number > 0:
                    res = c[number % jin] + res
                    number = number // jin
                
                ch_list = list(res)
                
        return ch_list
    
    i=0
    while len(ho) < m * t:
        ho = ho + change(n, i)
        i += 1
   
    
    ha = []
    
    for a in range(p-1,len(ho),m):
        ha.append(ho[a])
        if len(ha) == t:
            break
    
    
        
    
    answer = ''.join(ha)
    return answer