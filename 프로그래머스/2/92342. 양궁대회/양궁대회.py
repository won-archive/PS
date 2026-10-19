def solution(n, info):
    ryan = [0] * 11
    max_d = 0
    ans = [-1]
    
    def dfs(i, left):
        nonlocal max_d, ans
        
        if i == 11:
            if left:
                ryan[10] += left
            
            d = 0
            for j in range(11):
                if ryan[j] > info[j]:
                    d += 10 - j
                elif ryan[j] < info[j]:
                    d -= 10 - j
                    
            if d > 0 and (d > max_d or (d == max_d and ryan[::-1] > ans[::-1])):
                max_d = d
                ans = ryan[:]
            ryan[10] -= left
            return
        
        need = info[i] + 1
        if left >= need:
            ryan[i] = need
            dfs(i + 1, left - need)
            ryan[i] = 0
        dfs(i + 1, left)
        
    dfs(0, n)
    return ans