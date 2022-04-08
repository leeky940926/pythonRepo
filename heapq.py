import heapq 

heap = []

heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)

heapq.heappop()

heapq.heappushpop(9)

heapq.heapreplace(heap, 4)

heapq.heapify(heap)