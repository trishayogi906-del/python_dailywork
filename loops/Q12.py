# Q12. Given a list of numbers, stop printing when the number 0 is found. (Use break)
#○ Example: [3, 4, 1, 0, 7, 9] → stop at 0
numbers =input("enter numbers").split()
for i in numbers:
    if i=="0":
        break
    print(i)