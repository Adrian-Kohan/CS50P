# Getting a text from user
text = str(input("Text: "))

# Calculating the letters, words and sentences
c = 0
for i in text:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        c += 1

w = 1
for i in text:
    if i == " ":
        w += 1

s = 0
for i in text:
    if i == "." or i == "!" or i == "?":
        s += 1

# Calculating the grade
L = float(c * 100 / w)
S = float(s * 100 / w)
index = round(0.0588 * L - 0.296 * S - 15.8)

# Printing the grade
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")