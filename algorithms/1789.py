n = int(input())

i=1
while True:
    if (i*(i+1))/2 == n: 
        print(i) 
        break
    
    if (i*(i+1))/2 > n: 
        print(i-1)
        break
    i+=1
