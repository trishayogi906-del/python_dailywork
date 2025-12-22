# 14. Print numbers from 1 to 100 that contain the digit 3.
n=100
for i in range(1,n+1):
    num=i
    temp=0
    while(num>0):
        temp=num%10
        num//=10
        if temp==3:
            print(i)
