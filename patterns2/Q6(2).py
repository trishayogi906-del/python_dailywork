n=6
for i in range(n):
    
    for k in range(n-i):
        print(" ",end=" ")
    temp=1
    for j in range(i):
        print(temp,end=" ")
        temp+=1
    print()    