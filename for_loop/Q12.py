# 12. Find the sum of even numbers from 1 to 20.
n=20
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print("sum of even numbers from 1 to 20 = ",sum)        