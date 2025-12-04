import detectEnglish
import string
import multiplicativeCipher
import random
import utils
import affineCipher
import euclideans
if __name__ == "__main__":
    plain_text = r"hello, i want to encrypt this message!!!"
    plain_text2 = r"hello, i want to encrypt this message!!!()*+,-./:;<=>?@[\]^_`{|}啊"

    SYMBOL = string.printable
    length_symbol = len(SYMBOL)

    keyA, keyA_inverse = multiplicativeCipher.generateRandomKeys(length_symbol)
    print(keyA,keyA_inverse)
    keyB = random.randint(1,length_symbol-1)
    cipher_text = affineCipher.affineCipher("encrypt",keyA, 0, keyB, plain_text, SYMBOL)
    print(f"Encrypted: {cipher_text}")
    for key in range(1,length_symbol**2):
        keyA , keyB = utils.getKeyParts(key,length_symbol)
        keyA_inverse = euclideans.modular_multiplicative_inverse(keyA, length_symbol)
        if not keyA_inverse:
            continue
        decrypted_text = affineCipher.affineCipher("decrypt", 0, keyA_inverse, keyB, cipher_text,SYMBOL)
        if detectEnglish.is_english(decrypted_text):
            print(f"these are the keys")
            print(f"Key A: {keyA}")
            print(f"Key B: {keyB}")
            print(f"plain text is:\n{decrypted_text}")