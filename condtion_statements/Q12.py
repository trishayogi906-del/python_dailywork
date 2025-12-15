# Q12 Write a program that takes the name of a month as input and prints the number of days in that
 # month. Consider leap years for February.
 month = input("enter a month name in lower case ")
if month in ["january","march","may","july","august","October","december"]:
  print("in this month 31 days")
elif month in ["april","june","setepmber","November"]:
  print("in this month 30 days")
else:
  print("in this month 28 days ")  
