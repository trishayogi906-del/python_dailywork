# 11.Write a program to find the power of a number using for loop.
num=int(input("enter num: "))
power=int(input("enter power: "))
while(power!=0):
    num=num*power
    power-=1
print(num)    