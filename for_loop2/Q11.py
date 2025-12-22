# 11. Print numbers from 1 to 100 whose sum of digits is 5.
n=100

for i in range(1,n+1):
    temp=i
    sum=0
    
    while(temp!=0):
        sum=sum+(temp%10)
        temp//=10
    if sum==5:
        print(i)    
