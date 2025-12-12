# Q20.Print the Fibonacci series up to N terms using a for loop.
n=int(input("enter n :"))
first= 0
second=1
print(first)
print(second)
for i in range(n-2):
    nxt=first+second
    print(nxt)
    first=second
    second=nxt