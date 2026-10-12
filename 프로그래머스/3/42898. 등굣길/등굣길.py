def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    
    for x, y in puddles:
        dp[y - 1][x - 1] = -1
        
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if dp[i][j] != 0:
                continue
            a, b = 0, 0
            if 0 <= i - 1 < n and 0 <= j < m and dp[i - 1][j] != -1:
                a = dp[i - 1][j]
            if 0 <= i < n and 0 <= j - 1 < m and dp[i][j - 1] != -1:
                b = dp[i][j - 1]
            dp[i][j] = (a + b) % 1_000_000_007
    
    return dp[n - 1][m - 1]