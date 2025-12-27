# 15.Write a program to check whether a number is Prime number or not.
num =int(input("enter number: "))
i=2
count=0
while(i<num):
    if num%i==0:
        count=1
    i+=1
if count==0:
    print(f"{num} is prime number")
else:
        print(f"{num} is not prime number")    