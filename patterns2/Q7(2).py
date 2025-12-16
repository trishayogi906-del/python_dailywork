n=5
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    temp=65
    for j in range(i):
        print(chr(temp),end=" ")
        temp+=1
    print()    