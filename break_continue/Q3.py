# 3. Print numbers from 1 to 20, but stop when a number is divisible by 7.
n=20
for i in range(1,n+1):
    if i%7==0:
        break
    print(i)