
import pyfiglet as fig


import termcolor2 as colors


def asciiText(Message , color = "white"):
    msg = fig.figlet_format(Message)
    return colors.colored(msg , color=color)



