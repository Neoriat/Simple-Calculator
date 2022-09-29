# Calculator

def calculate(number1,number2,operand):
    if __operator__ == "+":  # Addition
        print(f"Your Answer Is {__firstNumber__ + __secondNumber__}")
    elif __operator__ == "-":  # SubTrack
        print(f"Your Answer Is {__firstNumber__ - __secondNumber__}")
    elif __operator__ == "*":  # Multiplation
        print(f"Your Answer Is {__firstNumber__ * __secondNumber__}")
    try:
        if __operator__ == "/":  # Division
            print(
                f"Your Answer Is {__firstNumber__ / __secondNumber__} And The Reamaning Of The Division Is {__firstNumber__ % __secondNumber__}")
    except ZeroDivisionError:
        raise ZeroDivisionError("ZeroDivisionError")
    if __operator__ == "**":  # Power
        print(f"Your Answer Is {__firstNumber__ ** __secondNumber__}")




if __name__ == '__main__':
    try:
        __firstNumber__ = int(input("Please Enter Your First Number :"))  # First Number Input
    except ValueError:
        raise ValueError("Please Enter A Number")
    __operator__ = input("What Operation You Want To Do? (Supported = + - * / **:")  # Opreator Input
    if __operator__ != "+" and __operator__ != "-" and __operator__ != "*" and __operator__ != "/" and __operator__ != "**":  # See If The Opreator Supported
        raise Exception(f"{__operator__} is not supported")
    try:
        __secondNumber__ = int(input("Please Enter Your Second Number :"))  # Second number input
    except ValueError:
        raise ValueError("Please Enter A Number")
    calculate(__firstNumber__,__secondNumber__,__operator__)






