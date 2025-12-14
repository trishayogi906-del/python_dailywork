# Q10 Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in
# kilograms) and height (in meters). Then categorize the BMI into:
weight = float(input("enter a weight in kilograms"))
height = float(input("enter a height in meters "))
bmi = weight/(height**2)

if(bmi<18.5):
  print("Underweight ")
elif(18.5 <= bmi < 24.9):
  print("Normal weight")
elif(25 <= BMI < 29.9):
  print("overweight") 
else:
  print("obesity")
