def solution(n, times):
    ans = 0
    
    l = 1
    r = max(times) * n
    while l <= r:
        mid = (l + r) // 2
        
        p = 0
        for t in times:
            p += mid // t
        
        if p >= n:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
        
    return ans