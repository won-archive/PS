from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    visited = [[1 if i == 0 else 0 for i in j] for j in maps]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[n - 1][m - 1]
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    return -1