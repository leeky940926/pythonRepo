n = int(input())

l=list()

for i in range(n):
    l.append(input())
    
l.sort(key=len)

r = max(l, key=len)

print(l)
print(r)
