import sys
from pyfiglet import Figlet


text = input("Input: ")

try:
    if len(sys.argv) == 2:
        f = Figlet(font=sys.argv[1])
        print (f.renderText(f"Output: {text}"))
    elif len(sys.argv) == 0:
        print (renderText(f"Output: {text}"))
except:
    print("Error")
    sys.exit
