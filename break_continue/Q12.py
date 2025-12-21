# 12. Print numbers from 1 to 100, skipping numbers whose square is divisible by 10.
n=100
for i in range(1,n+1):
    if i*i%10==0:
        break
    print(i)