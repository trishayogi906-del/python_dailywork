# Q2 Write a program that takes three numbers as input and prints the largest of the three.
num1 =int(input("enter num1: "))
num2 =int(input("enter num2: "))
num3 =int(input("enter num3: "))

if num1>num2 and num1>num3:
    print(f"{num1} is grater than {num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is grater than {num1} and {num3}")
else:
    print(f"{num3} is grater than {num1} and {num2}")      