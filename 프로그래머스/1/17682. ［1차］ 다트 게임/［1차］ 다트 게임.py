def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    result = []
    num = ''
    for d in dartResult:
        if d.isdigit():
            num += d
        elif d in bonus:
            result.append(int(num) ** bonus[d])
            num = ''
        elif d == '*':
            result[-1] *= 2
            if len(result) > 1:
                result[-2] *= 2
        else:
            result[-1] *= -1
            
    return sum(result)
    

# def solution(dartResult):
#     totalScore = [0, 0, 0]
#     results = [[] for _ in range(3)]
    
#     r = -1
#     for i, x in enumerate(dartResult):
#         if x.isdigit():
#             if dartResult[i-1].isdigit():
#                 results[r][0] = 10
#                 continue
#             r += 1
#             results[r].append(int(x))
#         else:
#             results[r].append(x)
    
#     sectionDic = {'S': 1, 'D': 2, 'T': 3}
#     for i, result in enumerate(results):
#         score, section, *option = result
#         totalScore[i] = score ** sectionDic[section]
#         if option:
#             if option[0] == '*':
#                 totalScore[i] *= 2
#                 if i != 0:
#                     totalScore[i-1] *= 2
#             else:
#                 totalScore[i] *= -1

#     return sum(totalScore)