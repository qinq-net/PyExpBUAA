#!/usr/bin/python3
# 1-5 Calculate the third edge of a right triangle
import math# should use some functions in 'math' module
try:
    # input the data
    bottom = float(input("Please input the bottom of the triangle: "))
    height = float(input("Please input the height of the triangle: "))
    if bottom > 0 and height > 0:# avoid non-positive numbers
        # the long edge's square equals to the sum of squares
        long = math.sqrt(bottom * bottom + height * height)
        print('The bottom of the triangle is:\t', bottom)# print out
        print("The height of the triangle is:\t",height)
        print("The third edge of thiangle is:\t",long)
    else:
        raise ValueError('edge cannot be non-positive:\t' + str(bottom) if bottom <= 0+ ' ' else ''+ str(height) if height <= 0 else '')
except Exception as exc:
    print("ERROR:\t", exc)