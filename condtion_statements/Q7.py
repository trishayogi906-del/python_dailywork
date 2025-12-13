# Q7 Write a program that takes a number as input and checks whether it is positive, negative, or zero.
num=int(input("enter anumber"))
if num>0:
    print(f"{num} is positive number")
elif num<0:
    print(f"{num} is negative number")
else:
    print(f"num is equal to '0'")        