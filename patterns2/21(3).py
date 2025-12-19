n=5

for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    temp=65    
    for j in range(2*i-1):
        if j==0  or j==2*i-2:
            print(chr(temp),end=" ")
        
        else:
            print(" ",end=" ")
        temp+=1           
    print()
          
for i in range(n-1,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    temp=65    
    for j in range(2*i-1):
        if j==0  or j==2*i-2:
            print(chr(temp),end=" ")
           
        else:
            print(" ",end=" ") 
        temp+=1         
    print()      