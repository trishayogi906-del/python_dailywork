''' Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based
on the following criteria:
>= 90: Grade A
>= 80: Grade B
>= 70: Grade C
>= 60: Grade D
< 60: Grade F '''
percantage =int(input("enter a percantage"))
if percantage>=90:
    print("Grade A")
elif percantage>=80:
    print("Grade B")   
elif percantage>=70:
    print("Grade C")
elif percantage>= 60:
    print("Grade D")
else:
    print("Grade F")    
