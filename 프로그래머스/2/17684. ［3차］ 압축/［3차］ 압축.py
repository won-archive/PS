def solution(msg):
    dic = {}
    idx = 1
    for n in range(65, 91):
        dic[chr(n)] = idx
        idx += 1
        
    ans = []
    w = ''
    for ch in msg:
        if (w + ch) not in dic:
            dic[w + ch] = idx
            ans.append(dic[w])
            w = ch
            idx += 1
        else:
            w += ch
            
    ans.append(dic[w])
    
    return ans