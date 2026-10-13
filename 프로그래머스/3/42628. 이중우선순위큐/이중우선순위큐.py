import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = {}
    
    for o in operations:
        c1, c2 = o.split()
        c2 = int(c2)
        
        if c1 == 'D':   # 삭제
            if c2 == 1:   # 최댓값 삭제
                while max_heap and not visited.get(-max_heap[0]):
                    heapq.heappop(max_heap)
                if max_heap:
                    num = heapq.heappop(max_heap)
                    visited[-num] -= 1
            else:           # 최솟값 삭제
                while min_heap and not visited.get(min_heap[0]):
                    heapq.heappop(min_heap)
                if min_heap:
                    num = heapq.heappop(min_heap)
                    visited[num] -= 1
        else:           # 삽입
            if visited.get(c2):
                visited[c2] += 1
            else:
                visited[c2] = 1
            heapq.heappush(min_heap, c2)
            heapq.heappush(max_heap, -c2)
    
    count = sum(visited.values())
    if count == 0:
        return [0, 0]
    
    while max_heap and not visited.get(-max_heap[0]):
        heapq.heappop(max_heap)
    while min_heap and not visited.get(min_heap[0]):
        heapq.heappop(min_heap)
    
    return [-max_heap[0], min_heap[0]]