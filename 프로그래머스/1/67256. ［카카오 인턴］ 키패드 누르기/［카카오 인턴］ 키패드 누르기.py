def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    
    def find_index(num):
        for i in range(4):
            for j in range(3):
                if num == keypad[i][j]:
                    return (i, j)
    
    left = (3, 0)
    right = (3, 2)
    ans = []
    for number in numbers:
        x, y = find_index(number)
        if y == 0:
            left = (x, y)
            ans.append('L')
        elif y == 2:
            right = (x, y)
            ans.append('R')
        else:
            l = abs(left[0] - x) + abs(left[1] - y)
            r = abs(right[0] - x) + abs(right[1] - y)
            if l < r:
                left = (x, y)
                ans.append('L')
            elif l > r:
                right = (x, y)
                ans.append('R')
            else:
                if hand == 'right':
                    right = (x, y)
                    ans.append('R')
                else:
                    left = (x, y)
                    ans.append('L')
                    
    return ''.join(ans)
