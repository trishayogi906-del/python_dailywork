# Q6 Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and
# performs the specified operation. Print the result based on the operation.
a=int(input("enter a number1 = "))
b=int(input("enter a number2 = "))

o=input("enter a arthmetic opertaor to perform operation ! = ")

if o=='+':
  print("a+b = ",a+b)
elif o=='-':
  print("a-b = ",a-b)
elif o=='*':
  print("a*b = ",a*b)
else:
  print("a/b = ",a/b)
