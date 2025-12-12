# Q3. Title Case Without split() or title()
# Convert an entire sentence into Title Case using loops only.
st = input("enter a string")
words = st.split()

for i in range(len(words)):
    w = words[i]

    if w[0].islower():
        words[i] = w[0].upper()+w[1:]
    else:
        words[i] = w

st = " ".join(words)
print( st)