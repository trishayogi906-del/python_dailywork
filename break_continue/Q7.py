# 7. Print numbers from 1 to 100, but stop when the sum of printed numbers exceeds 50.
sum=0
for i in range(1,101):
    sum=sum+i
    if sum>=50:
        break
    print(i)