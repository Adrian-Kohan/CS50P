greeting = input("Greeting: ").lower()

first_h = greeting[0]

if "hello" in greeting:
    print("$0")
elif first_h == "h":
    print("$20")
else:
    print("$100")