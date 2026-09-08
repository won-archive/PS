def solution(s):
    ans = len(s)
    max_unit = len(s) // 2
    unit = 1
    while unit <= max_unit:
        prev = ''
        cnt = 0
        ns = ''
        for i in range(0, len(s), unit):
            if prev == s[i:i+unit]:
                cnt += 1
            else:
                if cnt:
                    ns += f'{cnt + 1}{prev}'
                else:
                    ns += prev
                prev = s[i:i+unit]
                cnt = 0
        
        if cnt:
            ns += f'{cnt + 1}{prev}'
        else:
            ns += prev
    
        ans = min(ans, len(ns))
        
        unit += 1
    return ans

# AI 풀이
# def solution(s):
#     n = len(s)
#     ans = n                                   # 압축 안 한 길이가 상한
#     for unit in range(1, n // 2 + 1):
#         length = 0
#         prev, cnt = s[:unit], 1               # 첫 조각부터 시작, cnt는 실제 등장 횟수
#         for i in range(unit, n, unit):
#             cur = s[i:i+unit]
#             if cur == prev:
#                 cnt += 1
#             else:
#                 length += len(prev) + (len(str(cnt)) if cnt > 1 else 0)
#                 prev, cnt = cur, 1
#         length += len(prev) + (len(str(cnt)) if cnt > 1 else 0)
#         ans = min(ans, length)
#     return ans