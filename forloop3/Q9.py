# 9. Write a program to find the sum of first and last digit of a number.
num=int(input("enter a num :"))
last_digit = num%10
first_digit=0
while (num!=0):
    first_digit=num%10
    num//=10
sum=first_digit+last_digit
print(sum)    