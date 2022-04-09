'''
2839
'''

# n = int(input())
# a = n//5
# r = (n-5*a)//3
# l=list()

# for i in range(r+1):
#     x = (n-5*i)//3
    
#     if 3*x + 5*i == n:
#         l.append(x+i)

# print(l)

'''
11399
'''
# n = int(input())

# l = list(map(int, input().split()))
# ll=list()
# l.sort()

# a=0

# for i in l:
#     a += i
#     ll.append(a)
    
# print(sum(ll))
'''
11047
'''

# a = list(map(int, input().split()))

# n=a[0]
# k=a[1]

# l = list()
# for i in range(n):
#     l.append(int(input()))

# v = 0
# n = n-1
# while n>=0:
#     v += k//l[n]
#     k = k%l[n]
#     n-=1

# print(v)

'''
1931
'''
n = int(input())
l=list()

for i in range(n):
    l.append(list(map(int, input().split())))
    
cnt=1

l = sorted(l, key=lambda a:a[0])
#l = sorted(l, key=lambda a:a[1])

print(l)