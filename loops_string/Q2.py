# Q2. Palindrome Words
# Print all palindrome words found in a given sentence.
# ○ Example: "mom and dad went to civic center" -> output: mom dad civic
st = input("enter a string")
word=st.split()

for i in word:
  w=i.strip(".,!?;:-")
  if w == w[::-1] and len(w)>1:
    print(w)