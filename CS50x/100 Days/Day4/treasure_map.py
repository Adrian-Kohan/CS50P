
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n")

if position[1] == 1:
    row1[position[0] - 1] = "X"
elif position[1] == 2:
    row2[position[0] - 1] = "X"
else:
    row3[position[0] - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")



