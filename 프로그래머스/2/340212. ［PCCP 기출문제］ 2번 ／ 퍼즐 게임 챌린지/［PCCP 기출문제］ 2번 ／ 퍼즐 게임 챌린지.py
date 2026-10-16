def solution(diffs, times, limit):
    n = len(diffs)
    
    l = 1
    r = max(diffs)
    ans = 0
    while l <= r:
        m = (l + r) // 2
        
        tot = 0
        for i in range(n):
            if diffs[i] <= m:
                tot += times[i]
            else:
                tot += (times[i] + times[i - 1]) * (diffs[i] - m) + times[i]
                
        if tot <= limit:
            r = m - 1
            ans = m
        else:
            l = m + 1
        
    return ans