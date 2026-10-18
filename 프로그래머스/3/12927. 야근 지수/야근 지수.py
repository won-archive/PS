import heapq

def solution(n, works):
    # 남은 작업량이 없는 경우
    if sum(works) <= n:
        return 0
    
    arr = [-work for work in works]
    heapq.heapify(arr)
    
    for i in range(n):
        x = heapq.heappop(arr)
        heapq.heappush(arr, x + 1)
    
    return sum(x ** 2 for x in arr)