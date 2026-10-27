def solution(money):
    def max_money(arr):
        n = len(arr)
        dp = [0] * n

        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
        
        return dp[n - 1]
        
    return max(max_money(money[1:]), max_money(money[:-1]))