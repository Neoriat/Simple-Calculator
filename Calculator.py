

# Calculator


from ast import operator
from decimal import DivisionByZero
from typing import Type
from fig import asciiText

print(asciiText("Calculator"))

try:
    __firstNumber__ = int(input("Please Enter Your First Number :"))
except ValueError:
    raise ValueError("Please Enter A Number")


__operator__ = input("What Operation You Want To Do? (Supported = + - * / **:")

if __operator__ != "+" and  __operator__ != "-" and __operator__ != "*" and __operator__ != "/"  and __operator__ != "**":
    raise Exception(f"{__operator__} is not supported")

try:

    __secondNumber__ = int(input("Please Enter Your Second Number :"))
except ValueError:
    raise ValueError("Please Enter A Number")



if __operator__ == "+":

    print(f"Your Answer Is {__firstNumber__ + __secondNumber__}")


elif __operator__ == "-":

    print(f"Your Answer Is {__firstNumber__ - __secondNumber__}")


elif __operator__ == "*":

    print(f"Your Answer Is {__firstNumber__ * __secondNumber__}")

try:
    if __operator__ == "/":

        print(f"Your Answer Is {__firstNumber__ / __secondNumber__}")

except ZeroDivisionError:
    raise ZeroDivisionError("ZeroDivisionError")

if __operator__ == "**":

    print(f"Your Answer Is {__firstNumber__ ** __secondNumber__}")


input("Press Enter To Continue")



