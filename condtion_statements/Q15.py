# Q15 Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1
# for Monday, 2 for Tuesday, etc.).
day = int(input("enter a day number from 1-7 "))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")  
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday") 
elif day==5:
    print("firday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("Invaild number ! please enter 1- 7") 
                            
