# Q13. Write a program that simulates a simple ATM. The user should be able to:
# Check balance
# Deposit money
# Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user'
# choices.
balance = 2000

print("WELCOME TO SIMPLE ATM ")
print("1. check balance ")
print("2. Deposit money ")
print("3. Withdraw money ")

choice=int(input("enter your choice(1/2/3) = "))

if(choice==1):
  print("your current balance is : ",balance)
elif(choice==2):
  amount=float(input("enter your amount to Deposit "))
  balance+=amount
  print("Deposit succefull !")
  print("your current balance is : ",balance)
elif(choice==3):
  amount=float(input("enter your amount to withdraw ")) 
  if(amount <= balance):

   balance-=amount
   print("Wihtdraw succesfull !")
   print("Remaining balance is : ",balance)
  else:
   print("error : insufficent balance !")
else:
  print("Invalid choice !  please select 1 , 2 or 3")  


