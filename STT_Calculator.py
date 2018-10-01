#speech to text equation calculator

# 1) Accept speech input and convert it to a string
# 2) Split the string into a list of items
# 3) Iterate through each item in the list
# 4) Take each item and put it into a variable to be calculated
# 5) If the item is a number, just add it to the variable
# 6) If the item is a keyword (parentheses, minus, plus, divided by, etc), then convert that to the actual math symbol/function
#    - Create a dictionary of keywords with values being the math symbol corresponding to that key for easy conversion.
# 7) After the entire list has been iterated through, and the equation variable has been created, output the variable
#    as a string and then output the variable result.

import speech_recognition as sr
import win32com.client as wincl
import time

def calculate(eqtn):

	# Keyword dictionary (for powers of ("x to the power of"), you will need to grab the term prior to the power phrase so you can pow function it)
	keywords = {
	"open parentheses" : '(',
	"close parentheses" : ')',
	"minus" : '-',
	"plus" : '+',
	"divided by" : '/',
	"times" : '*',
	"to the power of" : '**'
	}

	itemList = []
	equation = ""

	eqtn = eqtn.split()  # Split the result into a list of items

	for e in eqtn:
		if e in keywords.keys():
			itemList.append(keywords.value(e))
		else:
			itemList.append(e)

	# After iteration is done, combine all the items in the item list into a variable for output
	for i in itemList:
		equation += str(i + " ")

	print("Equation: " + str(equation))
	print("Result of calculation: " + str(eval(equation)) + "\n")
