# k = int(input())
# w = list(map(int, input().split()))

# a=0
# l=[]
# for i in range(k):
#     l.append( (i+1)*w[i] )

# print(max(l))


k = int(input())
a=0
l=[]
m=[]

for i in range(k):
    l.append(int(input()))

l.sort(reverse=True)

for i,v in enumerate(l):
    m.append( (i+1)*l[i] )

print(max(m))