n=5
temp=n-1
for i in range(n):
    for j in range(temp): # for spaces
        print(" ",end=" ")
    for k in range(n):
        print("*",end=" ")
    print()  
    temp-=1      