def solution(board):
    r = len(board)
    c = len(board[0])
    
    dp = [[0] * c for _ in range(r)]
    for i in range(r):
        dp[i][0] = board[i][0]
    for j in range(c):
        dp[0][j] = board[0][j]
    
    for i in range(1, r):
        for j in range(1, c):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    ans = 0
    for i in range(r):
        ans = max(ans, max(dp[i]))
                
    return ans ** 2