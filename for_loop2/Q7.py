# 7. Print all numbers between 1 and 100 that are divisible by 6 but not by 12.
n=100
for i in range(1,n+1):
    if i%6==0 and i%12!=0:
        print(i)