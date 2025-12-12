# Q4. Prime Digits Count
# Take a numeric string and count how many digits are prime (2, 3, 5, 7).
st = input("enter a digit")

if st.isdigit():
    for i in st:
        num = int(i)

        if num > 1:
            count = 0
            for j in range(2, num):
                if num % j == 0:
                    count = 1
                    break

            if count == 0:
                print(num)
else:
    print("invalid input")