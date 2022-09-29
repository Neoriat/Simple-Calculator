
# Calculator

def calculate(firstNumber , secondNumber , operator):
    if operator == "+":

        return float(firstNumber) + float(secondNumber) , ""


    elif operator == "-":

        return float(firstNumber) - float(secondNumber) , ""


    elif operator == "*":

        return float(firstNumber) * float(secondNumber) , ""

    try:
        if operator == "/":

            

            return firstNumber / secondNumber ,  firstNumber % secondNumber
          

    except ZeroDivisionError:
       raise ZeroDivisionError("ZeroDivisionError")

    if operator == "**":

        return firstNumber ** secondNumber , "."


while True:

    if __name__ == '__main__':

        try:
            __firstNumber__ = float(input("Please Enter Your First Number:"))
        except ValueError:
            print("Please Enter A Number!")
            continue


        __operator__ = input("What Operation You Want To Do? (Supported = + - * / **:")

        if __operator__ != "+" and __operator__ != "-" and __operator__ != "*" and __operator__ != "/" and __operator__ != "**":
           print("Please Enter A Supported Operator!")
           continue

        try:

           __secondNumber__ = float(input("Please Enter Your Second Number :"))
        except ValueError:
           print("Please Enter A Number!")
           continue

        result , reminder   = calculate(__firstNumber__ , __secondNumber__ , __operator__)

        if __operator__ != "/":
    
            print(f'The Answer Is {result}')

        if __operator__ == "/":
            print(f'The Answer Is {result} And The Reminder Is {reminder}')


        userChoice = input("Do You Want To Calculate Anything Again?y/n:").lower()
        if userChoice == 'y':
            continue


        
        else: 
            break
