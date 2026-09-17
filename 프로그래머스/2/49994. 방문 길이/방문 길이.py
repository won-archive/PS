def solution(dirs):
    d = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    
    check = set()
    x, y = 0, 0
    for di in dirs:
        nx = x + d[di][0]
        ny = y + d[di][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road = tuple(sorted([(x, y), (nx, ny)]))
            check.add(road)
            x, y = nx, ny
    
    return len(check)