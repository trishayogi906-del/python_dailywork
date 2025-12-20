# 7. Print numbers from 1 to 50, skipping multiples of 5.
n=50
for i in range(1,n+1):
    if i%5 == 0:
        continue
    print(i)
