# 6. Write a program to count the number of digits in a number.
num=int(input("enter num :"))
count=0
while(num!=0):
    rem=num%10
    num//=10
    count+=1
print(count)    