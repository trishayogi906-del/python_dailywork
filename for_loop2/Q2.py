# 2. Print numbers from 1 to 50 whose last digit is 7.
n=50
for i in range(1,n+1):
    if i%10==7:
        print(i)