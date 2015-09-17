#!/usr/bin/python3
# 1-6 ASCII encoding
capital = input("Please input a CAPITAL letter: ")#input the letter
try:
	m = ord(capital)# get the ordinary code for the letter
	if m >= 65 and m <= 90:# consider if the letter is capital
		m = m + 32# convert to lower case
		low = chr(m)# convert to character
		print("The lower case is: ",low)# print out
	else:
		print("Please input a capital letter!")
except TypeError as exc:
	print("Please input only one character: ", exc)