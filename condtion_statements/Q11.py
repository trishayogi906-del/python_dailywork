# Q11. Write a program that calculates the discount for a product based on its price:
# If price is greater than 1000, discount is 10%
# If price is between 500 and 1000, discount is 5%
# Otherwise, no discount
# Print the final price after applying the discount.
price =int(input("enter price "))
if(price>1000):
  print("Discount 10%")
elif(price<=1000)or(500>=price):
  print("Discount 5%")
else:
  print("no discount")  
