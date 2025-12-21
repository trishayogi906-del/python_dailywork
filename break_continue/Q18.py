# 18. Print numbers from 1 to 50, skipping numbers that are perfect squares.
for i in range(1,51):
    root=i**0.5
    
    if root*root==i:
        continue
    print(i)