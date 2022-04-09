import heapq as h

heap = []

h.heappush(heap, 1)
h.heappush(heap, 2)
h.heappush(heap, 3)

h.heappop()

h.heappushpop(9)

h.heapreplace(heap, 4)

h.heapify(heap)