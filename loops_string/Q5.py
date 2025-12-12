#5. Sum of Digits in Alphanumeric String
#Add only the digits from the input string.
# ○ Example: "a1b4c2" -> Output: 7
# ○ Reverse String Without Slicing
# Reverse a string using loops only.

string=input("enter a string")
count=0
for i in string:
    if i.isdigit():
        count+=1
print(f"there are {count} digit in string")

# reverse string

rev = ""

for ch in string:
    rev = ch + rev

print("Reversed string:", rev)
