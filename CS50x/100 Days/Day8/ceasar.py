alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))
def caesar(sh, txt, direc):
    #create a new list that holds new encrypted alphabet
    #we just can duplicate our alphabet list [a-z,a-z] instead of doing the below
    new_alphabet = []
    for i in range(len(alphabet)):
        if (i + shift) < len(alphabet):
            new_alphabet += alphabet[i + shift]
        else:
            start = (i + shift) - len(alphabet)
            new_alphabet += alphabet[start]

    new_txt = ""
    if direc == "encode":
        for ch in txt:
            new_txt += new_alphabet[alphabet.index(ch)]
        print(f"The encoded text is: {new_txt}")

    elif direct == "decode":
        for ch in txt:
            new_txt += alphabet[new_alphabet.index(ch)]
        print(f"The decoded text is: {new_txt}")

    else:
        print("Please insert correct input")

caesar(sh = shift, txt = text, direct = direction)
