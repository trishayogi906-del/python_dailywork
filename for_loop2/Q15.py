# 15. Print the count of even numbers between 1 and 100 using a single loop.
n=100
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print(f"there are {count} even numbers between 1 to 100")        