# 18. Input a string and print if the reverse of the string is the same - using
# slicing (Palindrome Check).
st =input("enter a string ").strip()
if st == st[::-1]:
    print("string is palidrome ")
