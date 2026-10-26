def solution(m, n, puddles):
    MOD = 1_000_000_007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    p = set((x, y) for y, x in puddles)
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) == (1, 1) or (i, j) in p:
                continue
            
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    
    return dp[n][m]