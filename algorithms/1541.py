n = input().split("-")
l=[]
for i in n:
    a=0
    m = i.split("+")
    for j in m:
        a += int(j)
    l.append(a)

c = l[0] * 2 - sum(l)

print(c)