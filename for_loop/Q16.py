# 16. Count how many even numbers are there between 1 and 100.
n=100
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print(f"{count} even numbers between 1 to 100")        