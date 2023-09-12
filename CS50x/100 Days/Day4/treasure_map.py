
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n")
horizental = int(position[0]) - 1
vertical = int(position[1])
if vertical == 1:
    row1[horizental] = "🟨"
elif vertical == 2:
    row2[horizental] = "🟨"
elif vertical == 3:
    row3[horizental] = "🟨"

print(f"{row1}\n{row2}\n{row3}")



#or
#horizental = int(position[0])
#vertical = int(position[1])
#selected_row = map[vertical -1]
#selected_row[horezental -1] = "🟨"