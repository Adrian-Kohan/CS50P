alphabet: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'y', 'z']
direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
4
text = input("Type your message: \n").Lower()
5
shift = int(input("Type the shift number: \n"))
def encrypt(txt, shift):
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i + shift]
        for (i + shift) > len(alphabet):
            start = 
    for i in txt:
