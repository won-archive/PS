def solution(sequence):
    n = len(sequence)
    s1 = [sequence[i] * ((-1) ** i) for i in range(n)]
    s2 =[sequence[i] * ((-1) ** (i+1)) for i in range(n)]
    
    def best_sum(arr):
        dp = [0] * n
        
        dp[0] = arr[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
        
        return max(dp)
    
    return max(best_sum(s1), best_sum(s2))