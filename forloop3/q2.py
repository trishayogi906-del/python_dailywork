# run loop 400 to 250 count the number that are divisble by 11 and 13
count=0
for i in range(400,249,-1):
    if i%11==0 or i%13==0:
        count+=1
print(count)        