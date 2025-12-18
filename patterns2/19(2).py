n=5
for i in range(n,1,-1):
    
    for space in range(n - i):
        print(" ", end=" ")
    temp=65
    for star in range(2 * i - 1):
        print(chr(temp), end=" ")
        temp+=1
    print()
for i in range(1,n+1):
    
    for space in range(n - i):
        print(" ", end=" ")
    temp=65
    for star in range(2 * i - 1):
        print(chr(temp), end=" ")
        temp+=1
    print()    