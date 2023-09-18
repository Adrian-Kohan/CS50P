w = int(input("Width of wall: "))
h = int(input("Heigth of wall: "))
cover  = 5
def area_calculation(w, h, cover):
    number_of_cans = round((w * h) / cover)
    print(f"You'll need {number_of_cans} cans of paint")

area_calculation(w,h,cover)