plain_text = "this is a secret message"

cipher_text = ""
x = len(plain_text)-1

while x >= 0:
    cipher_text += plain_text[x]
    x -= 1


print(cipher_text)