#!/usr/bin/python3
# 1-3 Calculation Exercise
num = input("Input a natural number: ") #
try:
	num = int(num)# convert to integer
	if num >= 0:# avoid minus numbers
		print(((num + 2) * 3 - 6) / 3 == num)
	else:
		raise TypeError('minus')
except:
    print('Please input a natural number.')
