# 12. Print the largest number divisible by 9 between 1 and 100.
n=100
num=9
for i in range(1,n+1):
    if i%9==0:
        if i>num:
            num=i
print("largest number divisible by 9 between 1 to 100 : ",num)            