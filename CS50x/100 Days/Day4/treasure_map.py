
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n")
vertical = int(position[0]) - 1
horizental = int(position[1])
if horizental == 1:
    row1[vertical] = "🟨"
elif horizental == 2:
    row2[vertical] = "🟨"
elif horizental == 3:
    row3[vertical] = "🟨"

print(f"{row1}\n{row2}\n{row3}")



