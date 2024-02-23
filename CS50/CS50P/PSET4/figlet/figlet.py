import sys
import pyfiglet
import random


text = input("Input: ")
print(pyfiglet.figlet_format(f"Output: {text}"))

try:
    if len(sys.argv) == 2:
        f = Figlet(font=sys.argv[1])
        print(pyfiglet.figlet_format(f"Output: {text}", font=f))
    elif len(sys.argv) == 0:
        f = pyfiglet.figlet.setFont(font=random.choice(pyfiglet.figlet.getFonts()))
        print(pyfiglet.figlet_format(f"Output: {text}", font=f))
except:
    print("Error")
    sys.exit
