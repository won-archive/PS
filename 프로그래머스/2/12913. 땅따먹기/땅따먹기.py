def solution(land):
    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, N):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i - 1][x] for x in range(4) if x != j)

    return max(dp[N - 1])