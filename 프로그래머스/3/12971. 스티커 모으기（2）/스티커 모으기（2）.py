def solution(sticker):
    
    def line(s):
        prev2, prev1 = 0, 0 # n-2, n-1
        for num in s:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1
    
    if len(sticker) == 1:
        return sticker[0]
    
    return max(line(sticker[1:]), line(sticker[:-1]))