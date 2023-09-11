#  Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input ("What size pizza do you want? S, M, or L\n")
add_pepperoni = input ("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# Don't change the code above
#Write your code below this line
bill = 0
if size == S:
    bill = 15
    print("small pizza costs $15")
elif size == M:
    bill = 20
    print("small pizza costs $20")
else:
    bill = 25
    print("small pizza costs $25")

if add_pepperoni == Y:
    if size == S:
        bill += 2
    else:
        bill += 3

if extra_cheese == Y:
    bill +=1

print(f"your bill is {bill}")