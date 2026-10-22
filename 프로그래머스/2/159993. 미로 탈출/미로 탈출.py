from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 시작 지점, 출구, 레버 초기화
    start_x = start_y = end_x = end_y = lever_x = lever_y = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start_x, start_y = i, j
            if maps[i][j] == 'E':
                end_x, end_y = i, j
            if maps[i][j] == 'L':
                lever_x, lever_y = i, j
                
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    def bfs(sx, sy, ex, ey):
        visited = [[-1] * m for _ in range(n)]
        
        q = deque([(sx, sy)])
        visited[sx][sy] = 0

        while q:
            x, y = q.popleft()

            if x == ex and y == ey:
                return visited[ex][ey]

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
        
        return visited[ex][ey]    # 갈 수 없음
                    
    start_to_lever = bfs(start_x, start_y, lever_x, lever_y)
    if start_to_lever == -1:
        return -1
    
    lever_to_end = bfs(lever_x, lever_y, end_x, end_y)
    if lever_to_end == -1:
        return -1
    
    return start_to_lever + lever_to_end