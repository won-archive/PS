def solution(line):
    n = len(line)
    int_list = []
    for i in range(n):
        for j in range(i + 1, n):
            a, b, e = line[i]
            c, d, f = line[j]
            
            den = (a * d) - (b * c)
            if den == 0 or ((b * f) - (e * d)) % den or ((e * c) - (a * f)) % den:
                continue
            
            x = ((b * f) - (e * d)) // den
            y = ((e * c) - (a * f)) // den
            
            int_list.append((x, y))
            
    x_sort = sorted(int_list)
    y_sort = sorted(int_list, key=lambda x: x[1])
    min_x, max_x = x_sort[0][0], x_sort[-1][0]
    min_y, max_y = y_sort[0][1], y_sort[-1][1]
    
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    matrix = [['.'] * width for _ in range(height)]
    
    for x, y in int_list:
        matrix[max_y - y][x - min_x] = '*'
    
    return [''.join(m) for m in matrix]