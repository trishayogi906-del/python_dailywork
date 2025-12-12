# Q13. Check if a given number is prime or not using a for loop.
num =int(input("enter a num: "))
c=1
for i in range(2,num):
    if num%i==0:
        c=0
if c==1:
    print(f"{num} is prime number ")
else:
    print(f"{num} is not prime number ")
