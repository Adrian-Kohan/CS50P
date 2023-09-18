alphabet: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'y', 'z']
direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))
def encrypt(shift):
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i + shift]
        if (i + shift) > len(alphabet):
            start = (i + shift) - len(alphabet)
            alphabet[i] = alphabet[start]
    print(alphabet)

encrypt(shift)
