def solution(answers):
    length = len(answers)   # 문제 수
    p1 = [1, 2, 3, 4, 5] * (length // 5 + 1)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (length // 8 + 1)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (length // 10 + 1)
    
    result = [0, 0, 0]
    for i in range(length):
        if answers[i] == p1[i]:
            result[0] += 1
        if answers[i] == p2[i]:
            result[1] += 1
        if answers[i] == p3[i]:
            result[2] += 1
            
    maxValue = max(result)
    
    return [i+1 for i, r in enumerate(result) if r == maxValue]



# def solution(answers):
#     n = len(answers)
#     p1 = [1, 2, 3, 4, 5]
#     p2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
#     score = [0, 0, 0]
#     for i in range(n):
#         if answers[i] == p1[i % len(p1)]:
#             score[0] += 1
#         if answers[i] == p2[i % len(p2)]:
#             score[1] += 1
#         if answers[i] == p3[i % len(p3)]:
#             score[2] += 1
    
#     max_score = max(score)
#     answer = []
    
#     for i in range(3):
#         if score[i] == max_score:
#             answer.append(i+1)

#     return answer

# def solution(answers):
#     p1 = [1, 2, 3, 4, 5]
#     p2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

#     scores = [0, 0, 0]

#     for i, ans in enumerate(answers):
#         if ans == p1[i % len(p1)]:
#             scores[0] += 1
#         if ans == p2[i % len(p2)]:
#             scores[1] += 1
#         if ans == p3[i % len(p3)]:
#             scores[2] += 1

#     max_score = max(scores)
#     result = []

#     for i, score in enumerate(scores):
#         if score == max_score:
#             result.append(i + 1)

#     return result