#Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
# triangle. A triangle is valid if the sum of any two sides is greater than the third side.
# Check conditions like a + b > c, b + c > a, and a + c > b.
a = int(input("enter a num1 "))
b = int(input("enter a num1 "))
c = int(input("enter a num1 "))

if (a + b + c == 180):
  if(a + b > c) or (b + c > a) or (c + a > b):
    print("traingle is vaild ")
else :
  print("traingle is not vaild ")
