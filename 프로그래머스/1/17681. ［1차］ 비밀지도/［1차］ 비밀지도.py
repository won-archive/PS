def intToBin(n, arr):
    new_arr = []
    for num in arr:
        binary = bin(num)[2:]
        temp = n - len(binary)
        if temp > 0:
            binary = ('0' * temp) + binary
        new_arr.append(binary)
    return new_arr

def solution(n, arr1, arr2):
    new_arr1 = intToBin(n, arr1)
    new_arr2 = intToBin(n, arr2)
    
    ans = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if new_arr1[i][j] == '0' and new_arr2[i][j] == '0':
                temp += ' '
                continue
            temp += '#'
        ans.append(temp)
    
    return ans