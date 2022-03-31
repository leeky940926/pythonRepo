#300초 60초 10초
n = int(input())

a,b,c=0,0,0

if n%10 > 0 : 
    print(-1)

else:
    a = n//300
    b = (n%300)//60
    c = ((n%300)%60)//10

    print(a,b,c)