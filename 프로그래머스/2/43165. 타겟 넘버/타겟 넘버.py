def solution(numbers, target):
    n = len(numbers)
    ans = 0
    
    def dfs(i, s):
        nonlocal ans
        
        if i == n - 1:
            if s == target:
                ans += 1
            return
        
        dfs(i + 1, s - numbers[i + 1])
        dfs(i + 1, s + numbers[i + 1])

    dfs(-1, 0)
    
    return ans