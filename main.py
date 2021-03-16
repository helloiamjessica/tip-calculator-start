#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")
total_bill = input("What is your total bill? ")
try:
  tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
except ValueError:
  print("This is not a whole number")
try:
  bill_splitters = int(input("How many people to split the bill? "))
except ValueError:
  print("This is not a whole number")

#turning into a float and dropping the dollar sign of the bill amount
total_bill = float(total_bill.replace('$',''))
#bill_splitters = int(bill_splitters)

#Call str.format(number) with "{:.2f}" as str and a float as number to return a string representation of the number with two decimal places. Call print(string) with the formatted float-string as string to print the float.
ten_percent = (total_bill / bill_splitters) * 1.10
ten_percent_dec = "{:.2f}".format(ten_percent)

twelve_percent = (total_bill / bill_splitters) * 1.12
twelve_percent_dec = "{:.2f}".format(twelve_percent)

fifteen_percent = (total_bill / bill_splitters) * 1.15
fifteen_percent_dec = "{:.2f}".format(fifteen_percent)


if tip_percentage == 10:
   print(f"Each person should pay ${ten_percent_dec}")
elif tip_percentage == 12:
  print(f"Each person should pay: ${twelve_percent_dec}")
elif tip_percentage == 15:
  print(f"Each person should pay: ${fifteen_percent_dec}")

