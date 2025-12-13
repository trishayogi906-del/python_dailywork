# Q5 Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.
letter = input("enter a letter ")
vowel ="aeiouAEIOU"
if letter in vowel:
    print(f"{letter} is vowel")
else:
    print(f"{letter} is consonant")    