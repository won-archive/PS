def solution(n):
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    visited = [[0] * i for i in range(1, n + 1)]
    
    x = y = d = 0
    for v in range(1, n * (n + 1) // 2 + 1):
        visited[x][y] = v
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < n and 0 <= ny <= nx and visited[nx][ny] == 0):
            d = (d + 1) % 3
            nx, ny = x + dx[d], y + dy[d]
        x, y = nx, ny
    
    return [item for row in visited for item in row]