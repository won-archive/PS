from collections import deque

def solution(rows, columns, queries):
    matrix = [[(i * columns) + j + 1 for j in range(columns)] for i in range(rows)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    ans = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        
        x, y = x1, y1
        temp = deque([matrix[x][y]])
        d = 0
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx == x1 and ny == y1:
                break
            
            if x1 <= nx <= x2 and y1 <= ny <= y2:
                x, y = nx, ny
                temp.append(matrix[x][y])
            else:
                d = (d + 1) % 4
                
        temp.rotate(1)
        ans.append(min(temp))
        
        x, y = x1, y1
        matrix[x][y] = temp.popleft()
        d = 0
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx == x1 and ny == y1:
                break
            
            if x1 <= nx <= x2 and y1 <= ny <= y2:
                x, y = nx, ny
                matrix[x][y] = temp.popleft()
            else:
                d = (d + 1) % 4
    
    return ans