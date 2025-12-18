n=5
for i in range(n):
    temp=65
    for j in range(n):
       
        if i==0 or j==0 or j==n-1 or i==n-1:
            print(chr(temp),end=" ")
            
        else:
            print(" ",end=" ")
        temp+=1       
    print()            