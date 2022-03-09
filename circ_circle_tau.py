#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/08/2022
# Description: Calculates the circumference of a circle with user input

import constants
import math

# Calculation function that asks for input and calculates circumference
def calculate():
    # Loop that re asks for input if the user enters something invalid
    while True:
        num1 = input("Enter the radius of your circle:\n").strip()
        # checks to make sure input is valid
        try:
            rad = float(num1)
            break
        except ValueError:
            print(
                "Invalid Number. Please try again with no letters or special characters."
            )
    # Calcuating circumference
    circumference = constants.TAU * rad
    # displaying the circumference
    print("The circumference of your circle is {:.2f}cm".format(circumference))


# main function calls calculate function
def main():
    calculate()


# if statement calss main function
if __name__ == "__main__":
    main()
