# 10. Print numbers from 1 to 50, skipping numbers whose last digit is 5.
n=50
for i in range(1,n+1):
    if i%10==5:
        continue
    print(i)