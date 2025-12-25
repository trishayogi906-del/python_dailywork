# 10.Write a program to enter a number and print its reverse.
num=int(input("enter num : "))
revers=0
while(num!=0):
    rev=rev*10+(num%10)
    num//=10
print(revers)    