# Show a welcome note
print("Welcome to the tip calculator.")
# Ask for the bill
bill = int(input("What was the total bill? $"))
#Ask for the tip
tip = int(input("What percentage tip whould you like to give? 10 or 12 or 15? "))
#calculate the tip number
tip_to_pay = bill * tip/100
#Ask for the number of pepole that split the bill
number_of_people = int(input("How many people to split the bill? "))
#calculate each person's bill
bill_for_each_person = (bill + tip_to_pay) / number_of_people
#show them how much should pay
print(bill_for_each_person)