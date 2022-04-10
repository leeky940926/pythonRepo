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
# n = int(input())
# l=list()

# for i in range(n):
#     l.append(list(map(int, input().split())))

# l = sorted(l, key=lambda a:a[0])
# l = sorted(l, key=lambda a:a[1])
    
# cnt=0
# base = 0

# for i,j in l:
#     if i >= base:
#         base = j
#         cnt+=1

# print(cnt)

'''
1026
'''
# n=int(input())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# r=0

# a.sort()

# while n>0:
#     r += min(a) * max(b)
#     a.remove(min(a))
#     b.remove(max(b))
#     n-=1

# print(r)

'''
1541
'''
# n = input().split("-")
# l = list()
# for i in n:
#     r=0
#     a = i.split("+")
#     for j in a:
#         r+= int(j)
#     l.append(r)

# c = l[0] * 2 - sum(l)
# print(c)

'''
5585
'''
# n = int(input())
# n=1000-n

# l = [500, 100, 50, 10, 5, 1]

# a=0

# for i in l:
#     a += n//i
#     n -= i*(n//i)

# print(a)

'''
2217
'''
n=int(input())

l=list()
m=list()

a=0

for i in range(n):
    l.append(int(input()))
    
    #35 33 30 20 12
l.sort(reverse=True)

for i,v in enumerate(l):
    m.append((i+1)*v)

print(max(m))