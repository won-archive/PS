from collections import Counter
 
def solution(topping):
    a = Counter()
    b = Counter(topping)
    
    ans = 0
    for t in topping:
        a[t] += 1
        b[t] -= 1
        if b[t] == 0:
            del b[t]
        
        if len(a) == len(b):
            ans += 1
        
    return ans