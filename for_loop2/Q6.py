# 6. Print numbers from 1 to 50 that are perfect squares.
for i in range(2,50+1):
    root=i**0.5
    if root%1==0:
        print(i)