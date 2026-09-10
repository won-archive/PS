def solution(new_id):
    # 1
    new_id = new_id.lower()
    
    # 2
    new_id = ''.join(char for char in new_id if char.isalpha() or char.isdigit() or char in ['-', '_', '.'])
    
    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4
    new_id = new_id.strip('.')
    
    # 5
    if not new_id:
        new_id = 'a'
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15].strip('.')
    
    # 7
    temp = new_id[-1]
    while len(new_id) <= 2:
        new_id += temp
    
    return new_id



# def solution(new_id):
#     answer = ''
#     # 1
#     new_id = new_id.lower()
#     # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
#     # 5
#     if answer == '':
#         answer = 'a'
#     # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7
#     while len(answer) < 3:
#         answer += answer[-1]
#     return answer