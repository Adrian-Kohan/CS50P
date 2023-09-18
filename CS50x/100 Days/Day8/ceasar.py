alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))
def encrypt(sh, txt):
    #we just can duplicate our alphabet list [a-z,a-z] instead of doing the below
    new_alphabet = []
    for i in range(len(alphabet)):
        if (i + shift) < len(alphabet):
            new_alphabet += alphabet[i + shift]
        else:
            start = (i + shift) - len(alphabet)
            new_alphabet += alphabet[start]

    #and we can just use alphabet.index(ch) instead of some of the below code
    new_txt = ""
    for ch in txt:
        for i in range(len(new_alphabet)):
            if alphabet[i] == ch:
                new_txt += new_alphabet[i]

    print(f"The encoded text is: {new_txt}")

def decrypt(sh, txt):
    #we just can duplicate our alphabet list [a-z,a-z] instead of doing the below
    new_alphabet = []
    for i in range(len(alphabet)):
        if (i - shift) >= 0:
            new_alphabet += alphabet[i - shift]
        else:
            start = (i - shift) + len(alphabet)
            new_alphabet += alphabet[start]

    #and we can just use alphabet.index(ch) instead of some of the below code
    new_txt = ""
    for ch in txt:
        new_txt += alphabet[new_alphabet.index(ch)]


    print(f"The decoded text is: {new_txt}")


if direction == "encode":
    encrypt(sh = shift, txt = text)
elif direction == "decode":
    decrypt(sh = shift, txt = text)
else:
    print("Please insert correct input")

