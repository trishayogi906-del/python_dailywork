# 14.Write a program to find LCM of two numbers.
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
a=2
lcm=1
while(num1 != 1 or num2 != 1 ):
    if num1%a==0 or num2%a==0:
        if num1%a==0:
            print(a)
            num1=num1//a
        if num2%a==0:
            print(a)   
            num2=num2//a
        lcm*=a    
    else:
        a=a+1
print(lcm)

