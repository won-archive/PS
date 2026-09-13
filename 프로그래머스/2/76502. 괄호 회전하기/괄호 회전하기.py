from collections import deque

def solution(s):
    def rotate(x):
        stack = []
        for ch in x:
            if ch in '([{':
                stack.append(ch)
            elif ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return 0
            elif ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return 0
            else:
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return 0
        return 0 if stack else 1
    
    ns = deque(s)
    ans = 0
    for i in range(len(s)):
        if i != 0:
            temp = ns.popleft()
            ns.append(temp)
        ans += rotate(ns)
    
    return ans