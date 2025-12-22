# 9. Print numbers from 1 to 100 that are palindromes (single loop).
n=100
for i in range(1, n+1):
    if i>9:

        if str(i) == str(i)[::-1]:
            print(i)
