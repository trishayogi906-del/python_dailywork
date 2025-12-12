# Q18. Print only negative numbers from a given list.
numbers = list(map(int, input("Enter numbers: ").split()))

for n in numbers:
    if n < 0:
        print(n)

