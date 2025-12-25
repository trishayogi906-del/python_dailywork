# 7. Write a program to calculate the sum of digits of a number.
num=int(input("enter a num: "))
sum=0
while(num!=0):
    sum=sum+(num%10)
    num//=10
print(sum)    