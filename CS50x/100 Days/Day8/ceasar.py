alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))
def encrypt(sh, txt):
    new_alphabet = []
    for i in range(len(alphabet)):
        if (i + shift) < len(alphabet):
            new_alphabet += alphabet[i + shift]
        else:
            start = (i + shift) - len(alphabet)
            new_alphabet += alphabet[start]

    for i in range(len(alphabet)):
        new_txt = ""
        for ch in txt:
            if alphabet[i] == ch:
                new_txt += new_alphabet[i]

    print(new_alphabet)
    print(new_txt)

encrypt(sh = shift, txt = text)
