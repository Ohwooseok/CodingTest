def solution(files):
    def ssort(file):
        head = ""
        number = ""
        i = 0
        length = len(file)
        
        while i < length and not file[i].isdigit():
            head += file[i]
            i += 1
            
        
        cnt = 0
        while i < length and file[i].isdigit() and cnt < 5:
            number += file[i]
            i += 1
            cnt += 1
        
        return (head.lower(), int(number), files)
            
        
    files.sort(key = ssort)
    return files