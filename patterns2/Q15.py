n=4
for i in range(n):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()    

for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    
    for j in range(i):
        print("*",end=" ")
        
    print()        