import heapq 

n = int(input())

l = []
for _ in range(n):
    l.append(int(input()))

heapq.heapify(l)

a=0

while len(l) != 1:
    num1 = heapq.heappop(l)
    num2 = heapq.heappop(l)
    sum = num1 + num2
    a += sum
    heapq.heappush(l,sum)

print(a)