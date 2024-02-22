import sys
from pyfiglet import Figlet
import random


text = input("Input: ")

try:
    if len(sys.argv) == 2:
        f = Figlet(font=sys.argv[1])
        print (f.renderText(f"Output: {text}"))
    elif len(sys.argv) == 0:
        figlet = Figlet()
        figfonts = figlet.getFonts()
        random.seed()
        figlet.setFont(random.choice(figfonts))
        print (renderText(f"Output: {text}"))
except:
    print("Error")
    sys.exit
