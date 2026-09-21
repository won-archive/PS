from collections import deque

def solution(places):
    n = 5
    ans = [1] * n
    
    for i, place in enumerate(places):    # 대기실 순회
        room = [list(row) for row in place]
        candidates = [] # 응시자 위치
        for r in range(n):
            for c in range(n):
                if room[r][c] == 'P':
                    candidates.append((r, c))
                    
        # 응시자 없을 때
        if not candidates:
            continue
        
        for sx, sy in candidates:
            visited = set()
            
            if not ans[i]:
                break
            if room[sx][sy] == 'X':
                continue

            q = deque([(sx, sy, 0)])
            visited.add((sx, sy))
            while q:
                x, y, cnt = q.popleft()
                if not ans[i]:
                    break

                if cnt == 2:
                    continue

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n and room[nx][ny] != 'X' and (nx, ny) not in visited:
                        if room[nx][ny] == 'P':
                            ans[i] = 0
                            break
                        q.append((nx, ny, cnt + 1))
                        visited.add((nx, ny))
        
    return ans