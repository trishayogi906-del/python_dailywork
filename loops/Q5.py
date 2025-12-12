#Q5. Count how many numbers between 1 to 100 are divisible by 7.
count=0
for i in range(1,101):
    if i%7==0:
        count+=1
print(f"there are {count} multiple of 7 form 1 to 100")        

