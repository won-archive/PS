def solution(n, computers):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]:
                adj[i].append(j)
    
    visited = [0] * n
    def dfs(num):
        for a in adj[num]:
            if not visited[a]:
                visited[a] = 1
                dfs(a)
    
    ans = 0
    for k in range(n):
        if not visited[k]:
            ans += 1
            visited[k] = 1
            dfs(k)
    
    return ans