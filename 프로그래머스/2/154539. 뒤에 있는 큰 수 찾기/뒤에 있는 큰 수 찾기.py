def solution(numbers):
    n = len(numbers)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and stack[-1][1] < numbers[i]:
            idx, num = stack.pop()
            result[idx] = numbers[i]
        stack.append((i, numbers[i]))
    
    return result