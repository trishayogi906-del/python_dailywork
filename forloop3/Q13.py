# 13.Write a program to calculate the factorial of a number.
num=int(input("enter a num: "))
fact=1
while(num!=0):
    fact*=num
    num-=1
print(fact)