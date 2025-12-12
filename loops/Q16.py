# Q16. Count how many vowels are in the string: "Hello Python Programmer"
string="Hello Python Programmer"
vowel="aeiouAEIOU"
count=0
for i in string:
    if i in vowel:
        count+=1

print(f"total vowels are {count} in the given string")        