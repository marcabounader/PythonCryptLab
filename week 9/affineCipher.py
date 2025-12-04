import string
import multiplicativeCipher
import random
import sys
def affineCipher(mode: str, keyA: int, keyA_inverse: int, keyB: int, message: str, SYMBOL: str) -> str :
    text = ""
    length_symbol = len(SYMBOL)
    for chr in message:
        if chr in SYMBOL:
            index = SYMBOL.find(chr)
            if mode == "encrypt":
                shifted_index = (index * keyA + keyB) % length_symbol
            elif mode == "decrypt":
                shifted_index = (index - keyB)* keyA_inverse % length_symbol
            text += SYMBOL[shifted_index]
        else:
            text += chr
    return text

if __name__ == "__main__":
    plain_text = r"hello, i want to encrypt this message!!!()*+,-./:;<=>?@[\]^_`{|}啊"
    SYMBOL = string.ascii_letters + string.punctuation + "啊"
    length_symbol = len(SYMBOL)

    keyA, keyA_inverse = multiplicativeCipher.generateRandomKeys(length_symbol)
    keyB = random.randint(1,length_symbol-1)
    cipher_text = affineCipher("encrypt",keyA, keyA_inverse, keyB, plain_text, SYMBOL)
    print(f"Encrypted: {cipher_text}")
    plain_text = affineCipher("decrypt",keyA, keyA_inverse, keyB, cipher_text, SYMBOL)
    print(f"Decrypted: {plain_text}")