# 7. Input a username and check:
#    ○ If it contains a space → print "Invalid username"

#   ○ Else → print "Valid username"
st =input("enter a string")
if st == st.isspace():
    print("Invaild username")
else:
    print("Vaild username")
