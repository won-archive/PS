import itertools

def solution(number):
    ans = 0
    for c in itertools.combinations(number, 3):
        if sum(c) == 0:
            ans += 1
    
    return ans