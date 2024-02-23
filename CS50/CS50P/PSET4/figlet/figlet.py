import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(f"Output:\n{figlet.renderText(text)}")
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")


elif len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=random.choice(fonts))
    print(f"Output:\n{figlet.renderText(text)}")

else:
    sys.exit("Invalid usage")