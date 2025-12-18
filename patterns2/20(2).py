n=5
for i in range(n):
    temp=1
    for j in range(n):
       
        if i==0 or j==0 or j==n-1 or i==n-1:
            print(temp,end=" ")
            temp+=1 
        else:
            print(" ",end=" ")
          
    print()            