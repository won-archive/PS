def solution(m, n, board):
    new_board = [list(row) for row in board]
    
    ans = 0
    while True:
        blocks = set()
        # 2x2 형태 검사
        for i in range(m - 1):
            for j in range(n - 1):
                if new_board[i][j] != ' ' and new_board[i][j] == new_board[i][j+1] == new_board[i+1][j] == new_board[i+1][j+1]:
                    blocks.add((i, j))
                    blocks.add((i, j+1))
                    blocks.add((i+1, j))
                    blocks.add((i+1, j+1))

        if not blocks:
            break
            
        ans += len(blocks)
        for x, y in blocks:
            new_board[x][y] = ' '

        for c in range(n):
            temp = ''.join(new_board[r][c] for r in range(m) if not new_board[r][c] == ' ')
            d = m - len(temp)
            if d > 0:
                temp = (' ' * d) + temp
            for r in range(m):
                new_board[r][c] = temp[r]

    return ans