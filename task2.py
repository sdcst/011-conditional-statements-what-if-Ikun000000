#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""
X = float(input("The number"))
if X > 0:
    print("Positive")
if X == 0:
  print("Zero")
if X < 0:
   print("Negative")