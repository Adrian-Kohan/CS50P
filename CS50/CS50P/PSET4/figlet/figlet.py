import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

text = input("Input: ")

try:
    if len(sys.argv) == 2:
        font = Figlet.setFont(font=sys.argv[1])
        print(f"Output: {figlet.renderText(text, font=font)}")
    elif len(sys.argv) == 0:
        fonts = figlet.getFonts()
        font = figlet.setFont(font=random.choice(fonts))
        print(f"Output: {figlet.renderText(text, font=font)}")

except:
    print("Error")
    sys.exit
