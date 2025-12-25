# 8. Write a program to find the first and last digit of a number.
num=int(input("enter a num :"))
last_digit = num%10
first_digit=0
while (num!=0):
    first_digit=num%10
    num//=10
print("firts_digit of number = ",first_digit)
print("last_digit of number = ",last_digit)

                
                    
