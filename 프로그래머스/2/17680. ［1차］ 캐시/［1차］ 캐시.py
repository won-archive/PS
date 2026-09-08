from collections import deque

def solution(cacheSize, cities):
    ans = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            ans += 1
        else:
            ans += 5
        cache.append(city)
    
    return ans    



# 초기 구상 -> FIFO가 아닌 LRU를 구현해야 함
# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return len(cities) * 5
    
#     ans = 0
#     cache = []
#     for city in cities:
#         if city.upper() in cache:
#             ans += 1
#         else:
#             ans += 5
            
#         if len(cache) == cacheSize:
#             cache.pop(0)
        
#         cache.append(city.upper())
    
#     return ans