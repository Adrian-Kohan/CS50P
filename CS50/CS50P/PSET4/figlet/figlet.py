import sys
from pyfiglet import Figlet
import random

figlet = Figlet()



if len(sys.argv) == 2:
    if sys.argv[0] == "-f" or sys.argv[0] == "--font":
        text = input("Input: ")
        font = Figlet.setFont(font=sys.argv[1])

elif len(sys.argv) == 0:
    text = input("Input: ")
    fonts = figlet.getFonts()
    font = figlet.setFont(font=random.choice(fonts))

try:
    print(f"Output:\n{figlet.renderText(text)}")
except:
    print("Invalid usage")
    sys.exit
