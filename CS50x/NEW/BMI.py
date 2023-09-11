height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI= round(weight / height ** 2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, You are underwieght")
elif BMI < 25:
    print(f"Your BMI is {BMI},You have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI},You are overwieght")
elif BMI < 35:
    print(f"Your BMI is {BMI},You are obse")
else:
    print(f"Your BMI is {BMI},You are clinically obse")
