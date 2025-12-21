# 9. Print numbers from 1 to 100, but stop when a number is a multiple of 13.
for i in range(1,100+1):
    if i%13==0:
        break
    print(i)