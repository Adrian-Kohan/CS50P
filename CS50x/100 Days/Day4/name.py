import random
names_srting = input("Give me everybody's name, seperated by a comma. ")
names = names_srting.split(", ")
random_index = random.randint(0, len(names))
print(names[random_index])