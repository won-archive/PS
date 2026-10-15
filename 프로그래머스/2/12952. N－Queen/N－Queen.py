def solution(n):
    def cal(x, y):
        temp = {(x, y)}
        k = 1
        
        while k < n:
            dx = [k, k, k]
            dy = [k, 0, -k]
            
            for d in range(3):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    temp.add((nx, ny))
                    
            k += 1
        
        return temp
    
    ans = 0
    visited = []
    
    def dfs(i):
        nonlocal ans
        
        if i == n:
            ans += 1
            return
            
        for j in range(n):
            if all((i, j) not in v for v in visited):
                visited.append(cal(i, j))
                dfs(i + 1)
                visited.pop()
                
    dfs(0)
    
    return ans