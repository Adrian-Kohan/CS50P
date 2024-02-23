import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()




if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            text = input("Input: ")
            Figlet.setFont(sys.argv[2])
            print(f"Output:\n{figlet.renderText(text)}")
        else:
            print("Invalid usage")
            sys.exit
    else:
        print("Invalid usage")
        sys.exit

elif len(sys.argv) == 1:
    text = input("Input: ")
    font = figlet.setFont(font=random.choice(fonts))
    print(f"Output:\n{figlet.renderText(text)}")

else:
    print("Invalid usage")
    sys.exit
