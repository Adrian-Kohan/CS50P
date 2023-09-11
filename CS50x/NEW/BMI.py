height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI= round(weight / height ** 2)
if BMI < 18.5:
    print("You are underwieght")
elif 18.5 < BMI < 25:
    print("You have a normal weight")
elif 25 < BMI < 30:
    print("You are overwieght")
elif 30 < BMI < 35:
    print("You are obse")
else:
    print("You are clinically obse")
