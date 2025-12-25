# 5. Write a program to find the sum of all odd numbers between 1 to n.
num=int(input("enter num: "))
sum=0
i=1
while(i<=num):
    if i%2!=0:
        sum+=i
    i+=1
print(sum)        
    