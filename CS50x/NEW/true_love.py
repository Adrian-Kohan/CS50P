# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above
# Write your code below this line
lower_name1 = name1.lower()
lower_name2 = name2.lower()
T = lower_name1.count("t") + lower_name2.count("t")
R = lower_name1.count("r") + lower_name2.count("r")
U = lower_name1.count("u") + lower_name2.count("u")
E = lower_name1.count("e") + lower_name2.count("e")
total_true_score = str(T + R + U + E)
L = lower_name1.count("l") + lower_name2.count("l")
O = lower_name1.count("o") + lower_name2.count("o")
V = lower_name1.count("v") + lower_name2.count("v")
E = lower_name1.count("e") + lower_name2.count("e")
total_love_score = str(L + O + V + E)
love_score = int(total_true_score + total_love_score)
if love_score < 10 and love_score > 90:
    print(f"Your Score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your Score is {love_score}, you are alright together.")
else:
    print(f"Your Score is {love_score}.")


