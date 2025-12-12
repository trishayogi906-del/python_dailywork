# Q19. Reverse a string using a for loop.
#○ Example: "python" → "nohtyp
st = input("Enter a string: ")
rev = ""

for ch in st:
    rev = ch + rev   

print("Reversed string:", rev)
