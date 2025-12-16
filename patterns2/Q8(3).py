n=5
row=n
for i in range(n):
    for j in range(row): # for spaces
        print(" ",end=" ")
    temp=65    
    for k in range(n):
        print(chr(temp),end=" ")
        temp+=1
    print()  
    row-=1      