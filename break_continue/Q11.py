# 11. Print numbers from 1 to 30, but stop when the number is a perfect square.
for i in range(2,31):
    root=i**0.5
    
    if root%i==0:
        break
    print(i)