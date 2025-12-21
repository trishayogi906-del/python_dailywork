# 17. Print numbers from 1 to 100, but stop when a number is divisible by both 8 and 12.
n=100
for i in range(1,n+1):
    if i%8==0 and i%12==0:
        break
    print(i)