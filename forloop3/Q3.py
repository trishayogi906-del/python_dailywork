# run for loop 60 to 170 and get the total of number along with divisble by 9
sum=0
for i in range(60,171):
    if i%9==0:
        sum+=i
print(sum)        