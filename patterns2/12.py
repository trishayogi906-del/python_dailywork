n = 5
for i in range(1,n):
    
    for k in range(n - i):
        print(" ", end="")
    
    for j in range(2 * i - 1):
        if  j==0 or i==n-1 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()
