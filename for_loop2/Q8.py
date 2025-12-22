# 8. Print the count of numbers divisible by 7 between 1 and 100.
n=100
count=0
for i in range(1,n+1):
    if i%7 == 0:
        count+=1
print(f"there are {count} divisible of 7 between 1 to 100")        