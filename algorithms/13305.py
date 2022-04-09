n = int(input())
l = list(map(int, input().split()))
p = list(map(int, input().split()))

# for i in range(n-1):
#     l.append(int(input()))

# for i in range(n):
#     p.append(int(input()))
    
a=0
cost = p[0]

for i in range(n-1):
    if cost > p[i]:
        cost = p[i]
    a += cost * l[i]

print(a)
    