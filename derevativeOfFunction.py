__athor__ = "Trang Ha"

# Input: function, starting value, ending value, increment value
# Output: calculating derivative of the function and f(x) prime values

from numpy import arange
from sympy import Symbol, Derivative
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
from astropy.io import ascii

class NumericDerivative:

    def __init__(self, function, start, stop, step):
        self.function = function
        self.startValue = start
        self.stopValue = stop
        self.increment = step
        self.lst_xValue = []
        self.lst_fx = []
        self.lst_fxPrime = [0.0]

    # Function to store x value into a list
    def appendXValues(self):
        for numbers in arange(self.startValue, self.stopValue, self.increment):
            self.lst_xValue.append(numbers)
        print("List of x values: \n{0}".format(self.lst_xValue))

    def mainFunction(self):
        unknown = Symbol("x")
        fx = parse_expr(self.function)
        fxPrime = Derivative(self.function, unknown)

        # Print f(x) and f'(x) functions
        print("_______________________")
        print("f(x) = {0}".format(fx))
        print("f'(x) = {0}".format(fxPrime.doit()))
        print("________________________")

        # Solve for f(x) value
        for xValues in self.lst_xValue:
            # Replace unknown by x values and get f(x)
            fxValues = round(fx.doit().subs({unknown:xValues}), 3)
            self.lst_fx.append(fxValues)

        #Solve for f'(x) = (y2 - y1)/(x2 - x1)
        for index in range(0, len(self.lst_fx)-1):
            fxPrimeValues = round((self.lst_fx[index+1] - self.lst_fx[index]) / (self.lst_xValue[index+1] - (self.lst_xValue[index])),5)
            self.lst_fxPrime.append(fxPrimeValues)

        print("List of f(x): \n{0}".format(self.lst_fx))
        print("\n")
        print("List of f'(x): \n{0}".format(self.lst_fxPrime))

    def exportFile(self):
        xVal = np.array(self.lst_xValue)
        fxVal = np.array(self.lst_fx)
        fxPrimeVal = np.array(self.lst_fxPrime)
        ascii.write([xVal, fxVal, fxPrimeVal], "testFile.txt", names=["x", "f(x)", "f'(x)"])
        print("Exported file!")



while True:
    # Ask user for input values
    inputFunc = input("f(x) = ")
    startValue = float(input("Enter start value: "))
    stopValue = float(input("Enter stop value: "))
    increment = float(input("Enter delta X: "))

    # Execute the Numeric Derivative object with user input values
    obj1 = NumericDerivative(inputFunc, startValue, stopValue, increment)
    obj1.appendXValues()
    obj1.mainFunction()
    obj1.exportFile()

    # Ask user if continue or or break the loop
    respond = input("Continue or break (c = Continue; b = Break)? ")
    if respond == "c":
        continue
    elif respond == "b":
        break
    else:
        print("Invalid!!!")
