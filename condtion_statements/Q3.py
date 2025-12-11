# Q3 Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100
#unless it is also divisible by 400.

year=int(input("enter a year"))
if year%4==0 or year%400==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")    