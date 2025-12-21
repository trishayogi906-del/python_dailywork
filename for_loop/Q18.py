# 18. Print numbers from 1 to 20, but do not print 10.
n=20
for i in range(1,n+1):
    if i==10:
        continue
    print(i)