# 6. Print numbers from 1 to 30, skipping numbers divisible by 3.
n=30
for i in range(1,n+1):
    if i%3 == 0:
        continue
    print(i)