plain_text = "this is a secret message"

cipher_text = ""

for x in range(len(plain_text)-1,-1,-1):
    print(x)
    cipher_text += plain_text[x]
