# Q15. Print the smallest number in a list.
numbers = list(map(int, input("Enter numbers: ").split()))

small = numbers[0]  

for n in numbers:
    if n < small:
        small = n

print("Smallest number is:", small)
