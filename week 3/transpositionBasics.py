from math import ceil

plain_text = "I love abbas, but abbas doesn't love me"
key = 4
cipher_text = ""

def encrypt(key,plain_text):
    cipher_text = ""
    for col in range(key):
        pointer = col
        while pointer <= len(plain_text) -1:
            cipher_text+=plain_text[pointer]

            pointer += key

    return cipher_text

def decrypt(key,cipher_text):
    plain_text = ""
    col = ceil(len(cipher_text) / key)
    for c in range(col):
        pointer = c
        while pointer <= len(cipher_text) -1:
            plain_text+=cipher_text[pointer]
            pointer += col

    return plain_text



if __name__ =="__main__":
    encypted_text = encrypt(key,plain_text)
    print(f"Original: {plain_text}\nDecrypted text: {decrypt(key,encypted_text)}")

