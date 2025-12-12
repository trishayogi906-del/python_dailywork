# Q9. Take 10 numbers from the user and print the highest number.
larg=0
for i in range(10):
    num=int(input("enter a num : "))
    if num>larg:
        larg=num

print(larg)        