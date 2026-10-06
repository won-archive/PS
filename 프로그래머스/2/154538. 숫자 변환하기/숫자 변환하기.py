def solution(x, y, n):
    dp = [-1] * (y + 1)
    
    dp[x] = 0
    for i in range(x, y + 1):
        temp = []
        if i - n >= 0 and dp[i - n] != -1:
            temp.append(dp[i - n])
        if i % 2 == 0 and dp[i // 2] != -1:
            temp.append(dp[i // 2])
        if i % 3 == 0 and dp[i // 3] != -1:
            temp.append(dp[i // 3])
            
        if temp:
            dp[i] = min(temp) + 1
    
    return dp[y]