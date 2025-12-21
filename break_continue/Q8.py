# 8. Print numbers from 1 to 20, skipping numbers divisible by 4 or 6.
n=20
for i in range(1,n+1):
    if (i%4==0) or (i%6==0):
        continue
    print(i)