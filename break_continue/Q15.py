# 15. Print numbers from 1 to 50, but stop when the number contains the digit 9.
n=50
for i in range(1,n+1):
    if i==9:
        break
    print(i)