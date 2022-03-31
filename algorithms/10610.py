n = str(input())

n = ''.join(sorted(n, reverse=True))

n = int(n)

if n % 30 != 0:
    print(-1)
else:
    print(n)
    
