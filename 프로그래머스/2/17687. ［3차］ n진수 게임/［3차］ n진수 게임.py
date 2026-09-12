def solution(n, t, m, p):
    total = ''
    digits = "0123456789ABCDEF"
    for i in range(t * m):
        temp = '0' if i == 0 else ''
        while i > 0:
            temp = digits[i % n] + temp
            i //= n
        total += temp
    
    cnt = 0
    ans = ''
    for j in range(p-1, len(total), m):
        ans += total[j]
        cnt += 1
        if cnt == t:
            break
    
    return ans