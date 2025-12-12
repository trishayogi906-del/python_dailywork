# Q1. Vowel-based Word Count
# Count how many words in a sentence start AND end with a vowel
# (case-insensitive).
st = input("enter a string ")
count=0
vowel="aeiouAEIOU"
word=st.split()

for w in word:
    w = st.strip(".,!?;:-")
    if len(w)>0 and w[0] in vowel and w[-1] in vowel:
      count += 1


if count>0:
  print(count)
else:
  print("please start string from AND end with vowel")
