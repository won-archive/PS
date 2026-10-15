def solution(k, dungeons):
    n = len(dungeons)
    visited = [0] * n
    ans = 0
    
    def dfs(curr, cnt):
        nonlocal ans
        ans = max(ans, cnt)
        
        for i in range(n):
            if curr >= dungeons[i][0] and visited[i] == 0:
                visited[i] = 1
                dfs(curr - dungeons[i][1], cnt + 1)
                visited[i] = 0
    
    dfs(k, 0)
    
    return ans