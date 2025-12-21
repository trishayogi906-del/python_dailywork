# 4. Print numbers from 1 to 20, skipping all even numbers.
n=20
for i in range(1,n+1):
    if i%2==0:
        continue
        
    print(i)