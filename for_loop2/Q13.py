# 13. Print numbers from 1 to 50 that are divisible by 3 or 7 but not both.
n=50
for i in range(1,n+1):
    div_3 = i%3==0 
    div_7 = i%7==0 
    if div_3 != div_7:
        print(i)