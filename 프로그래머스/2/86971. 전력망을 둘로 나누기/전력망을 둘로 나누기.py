def solution(n, wires):
    def dfs(v1):
        for v2 in adj[v1]:
            if v2 not in visited:
                visited.add(v2)
                dfs(v2)  
    
    ans = n
    for i in range(n-1): # 끊을 전선
        adj = [[] for _ in range(n+1)]
        for j, (v1, v2) in enumerate(wires):
            if j == i:
                continue
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visited = set()
        visited.add(1)
        dfs(1)
        ans = min(ans, abs((n - len(visited)) - len(visited)))
        
    return ans