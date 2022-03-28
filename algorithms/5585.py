#1000 - input한 금액의 최소개수
n = int(input())
n = 1000 - n

a = 0

while n>0:
    if n>=500:
        a+=n//500
        n = n%500
    
    if n>=100:
        a+=n//100
        n = n%100
    
    if n>=50:
        a+=n//50
        n = n%50
    
    if n>=10:
        a+=n//10
        n = n%10
    
    if n>=5:
        a+=n//5
        n = n%5
    
    if n>=1:
        a+=n//1
        n = n%1

print(a)