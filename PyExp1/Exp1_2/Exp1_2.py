#!/usr/bin/python3
# 1-2 BMI calculation
weight = input("Please input your weight(kg): ")
height = input("Please input your height(m): ")
a = False
# Type Transport
try:
    weight = float(weight)
    height = float(height)
    if (weight <= 0) or (height < 0):# avoid minus number
        print("Input data cannot be minus.")
        a = True
except Exception as exc:
    print("Translation Error.", str(exc))
    a = True
if not a:
    # Calculating BMI
    try:
        BMI = weight / (height * height)
    except Exception as exc:
        print("Calculation Error.", str(exc))
    # Printing out BMI
    try:
        print("Your BMI is: ",BMI)
    except Exception as exc:
        print("An unknown error has occurred.", str(exc))
