# 15. Count and print vowels by iterating through the string.
st=input("enter a input")
a = "aieouAIEOU"
c=0
for i in st:
    if i in a:
        c+=1
        print(i)
print("vowels are :",c)
