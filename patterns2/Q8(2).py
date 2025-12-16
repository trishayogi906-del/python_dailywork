n=5
row=n
for i in range(n):
    for j in range(row): # for spaces
        print(" ",end=" ")
    temp=1
    for k in range(n):
        print(temp,end=" ")
        temp+=1
    print()  
    row-=1      