import sys
from pyfiglet import Figlet
from random import 

figlet = Figlet()
fonts = figlet.getFonts()




if len(sys.argv) == 2:
    if sys.argv[0] == "-f" or sys.argv[0] == "--font":
        if sys.argv[1] in fonts:
            text = input("Input: ")
            font = Figlet.setFont(font=sys.argv[1])
            print(f"Output:\n{figlet.renderText(text)}")
        else:
            print("Invalid usage")
            sys.exit
    else:
        print("Invalid usage")
        sys.exit

elif len(sys.argv) == 0:
    text = input("Input: ")
    font = figlet.setFont(font=random.choice(fonts))
    print(f"Output:\n{figlet.renderText(text)}")

else:
    print("Invalid usage")
    sys.exit
