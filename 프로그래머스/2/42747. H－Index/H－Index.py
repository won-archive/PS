def solution(citations):
    arr = sorted(citations, key=lambda x: -x)
    
    ans = 0
    for i, h in enumerate(arr):
        if h >= i + 1:
            ans = i + 1
    
    return ans