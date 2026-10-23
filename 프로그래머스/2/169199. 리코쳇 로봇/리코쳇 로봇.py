from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    
    # 출발/도착 위치 초기화
    sx = sy = ex = ey = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                sx, sy = i, j
            if board[i][j] == 'G':
                ex, ey = i, j          
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[-1] * m for _ in range(n)]
    
    q = deque([(sx, sy)])
    visited[sx][sy] = 0
    while q:
        x, y = q.popleft()
        
        if x == ex and y == ey:
            break
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'D':
                while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'D':
                    nx += dx[d]
                    ny += dy[d]
                nx -= dx[d]
                ny -= dy[d]
                if visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
            
    return visited[ex][ey]