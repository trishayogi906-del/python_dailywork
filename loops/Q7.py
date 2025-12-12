# Q7. Given a string, print the first 5 characters only and stop. (Use break)
string=input("enter a string ")
for i in string:
    print(i)
    if i==string[4]:
        break
