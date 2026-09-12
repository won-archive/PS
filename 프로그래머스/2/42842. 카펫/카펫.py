def solution(brown, yellow):
    total = brown + yellow
    
    for y in range(3, int(total ** 0.5) + 1):
        if total % y == 0:
            x = total // y
            if (x - 2) * (y - 2) == yellow:
                return [x, y]
    
    
    
    


# def solution(brown, yellow):
#     total = brown + yellow
    
#     for h in range(3, int(total ** 0.5) + 1):
#         if total % h == 0:
#             w = total // h
            
#             if (w - 2) * (h - 2) == yellow:
#                 return [w, h]

# 4 -> 최소 1 이상 되야 하기 때문에 3부터 시작, 약수는 항상 쌍으로 존재하기 때문에 **0.5
# 5 -> h가 약수인지 확인

# def solution(brown, yellow):
#     tot = brown + yellow
    
#     for i in range(3, tot+1):
#         if i < tot//i:
#             continue
#         if not tot%i:
#             x = i
#             y = tot//i
#             # print(x, y, tot%i)
#             if (x-2)*(y-2) == yellow:
#                 answer = [x, y]
#                 break

#     return answer