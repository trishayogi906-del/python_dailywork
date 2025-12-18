# hollow inverted half pyramid
for i in range(5,0,-1): 
    temp=1
    for j in range(i):
        if (j==0) or (i==5) or (j==i-1):

            print(temp,end=" ")
           
        else:
            print(" ",end=" ")   
        temp+=1      
    print()    