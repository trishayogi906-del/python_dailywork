# 5. Print the difference between the sum of even and odd numbers from 1 to 20.
n=20
sum_even=0
sum_odd=0
for i in range(1,n+1):
    if i%2==0:
        sum_even += i
    else:
        sum_odd+=i
print("Difference between sum of even and odd numbers ")
print("sum of even numbers 1 to 20 : ",sum_even)
print("sun of odd numbers 1 to 20 : ",sum_odd)           
