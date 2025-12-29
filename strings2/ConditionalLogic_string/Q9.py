# 9. Write a program to classify the string:
#  ○ Only alphabets → "Alphabetic"
#  ○ Only digits → "Numeric"
#  ○ Alphanumeric (mix of both) → "Alphanumeric"
st=input("enter a string")
if st.isalpha():
    print("Alphabaetic")
elif st.isdigit():
    print("numeric")
else:
    print("mix of both")        

