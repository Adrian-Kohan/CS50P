import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

text = input("Input: ")


if len(sys.argv) == 2:
    font = Figlet.setFont(font=sys.argv[1])
elif len(sys.argv) == 0:
    fonts = figlet.getFonts()
    font = figlet.setFont(font=random.choice(fonts))

try:
    print(f"Output:\n{figlet.renderText(text)}")
except:
    print("Invalid usage")
    sys.exit
