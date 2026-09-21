from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    new_maps = [list(row) for row in maps]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    ans = []
    for r in range(n):
        for c in range(m):
            if new_maps[r][c] == 'X':
                continue
                
            s = int(new_maps[r][c])  # 무인도 식량 수
            q = deque([(r, c)])
            new_maps[r][c] = 'X'
            
            while q:
                x, y = q.popleft()
                
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and new_maps[nx][ny] != 'X':
                        s += int(new_maps[nx][ny])
                        q.append((nx, ny))
                        new_maps[nx][ny] = 'X'
            ans.append(s)

    return sorted(ans) if ans else [-1]