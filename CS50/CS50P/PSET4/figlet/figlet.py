import sys
from pyfiglet import Figlet
import random


text = input("Input: ")

try:
    if len(sys.argv) == 2:
        f = Figlet(font=sys.argv[1])
        print(pyfiglet.figlet_format(f"Output: {text}", font=f))
    elif len(sys.argv) == 0:
        figlet = Figlet()
        figfonts = figlet.getFonts()
        f = figlet.setFont(font=random.choice(figfonts))
        print(pyfiglet.figlet_format(f"Output: {text}", font=f))
except:
    print("Error")
    sys.exit
