def solution(board, moves):
    n = len(board)
    
    ans = 0
    stack = []
    for move in moves:
        position = move - 1
        for i in range(n):
            if board[i][position]:
                if stack and stack[-1] == board[i][position]:
                    stack.pop()
                    board[i][position] = 0
                    ans += 2
                else:
                    stack.append(board[i][position])
                    board[i][position] = 0
                break
                
    return ans