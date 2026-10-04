import heapq

def solution(scoville, K):
    arr = scoville[:]
    heapq.heapify(arr)
    count = 0
    while True:
        m1 = heapq.heappop(arr)
        if m1 >= K:
            return count

        if len(arr) < 1:
            break
        
        m2 = heapq.heappop(arr)

        new = m1 + 2 * m2
        heapq.heappush(arr, new)
        
        count += 1
    
    return -1