def solution(prices):
    n = len(prices)
    ans = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                ans[i] += 1
            else:
                ans[i] += 1
                break
    
    return ans