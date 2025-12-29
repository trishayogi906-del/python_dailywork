# 12. Ask for a number (string input). If it is a digit, convert it to an integer and print the square of the number.
num=input("enter a number")
if num.isdigit():
    num=int(num)
    print(num*num)
else:
    print("not a number")
