# hollow half pyramid
n=5
for i in range(n):
    temp=1
    for j in range(i+1):
        if (j==0) or(i==j) or (i==n-1):
            print(temp,end=" ")  
        else:
            print(" ",end=" ")
            
        temp=temp+1
    print()            