def solution(want, number, discount):
    products = {}
    for k in range(len(want)):
        products[want[k]] = number[k]
    
    ans = 0
    for i in range(len(discount) - 10 + 1):
        temp = dict(products)
        for j in range(i, i + 10):
            if temp.get(discount[j]):
                temp[discount[j]] -= 1
        
        if sum(temp.values()) == 0:
            ans += 1
    
    return ans