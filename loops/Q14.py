#Q14. Print the factorial of a number using a for loop.
#○ Example: 5 → 120
num=int(input("enter a num "))
fact=1
num1=num
for i in range(num1):
    fact=fact*num
    num=num-1
print(f"factorial of {num1} is = ",fact)    