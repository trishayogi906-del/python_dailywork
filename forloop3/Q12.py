# 12.Write a program to find all factors of a number.
num=int(input("enter num: "))
orginal=num
i=2
while(i<=num):
    if num%i==0:
        print("factor: ",i)
        num=num//i
    else:
        i+=1