
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n")
vertical = int(position[0]) - 1
if position[1] == 1:
    row1[vertical] = "X"
elif position[1] == 2:
    row2[vertical] = "X"
else:
    row3[vertical] = "X"

print(f"{row1}\n{row2}\n{row3}")



