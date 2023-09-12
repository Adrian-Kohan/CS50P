import random
names_srting = input("Give me everybody's name, seperated by a comma. ")
names = names_srting.split(", ")
random_name = random.randint(0, len(names))
print(random_name)