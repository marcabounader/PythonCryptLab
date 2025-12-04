import euclideans
import string
import random



def generateRandomKeys(length_symbol):
    
    keyA = random.randint(2,length_symbol-1)
    try: 
        keyA_inverse = euclideans.modular_multiplicative_inverse(keyA, length_symbol)
        return keyA, keyA_inverse
            
    except Exception as e:
        print(f"This is the error: {e} with key {keyA}")
        generateRandomKeys(length_symbol)

def multiplicative_cipher(keyA: int, length_symbol: int, message: str) -> str :
    text = ""
    for chr in message:
        if chr in SYMBOL:
            index = SYMBOL.find(chr)
            shifted_index = (index * keyA) % length_symbol
            text += SYMBOL[shifted_index]
        else:
            text += chr
    return text

if __name__ == "__main__":
    plain_text = r"hello, i want to encrypt this message!!!()*+,-./:;<=>?@[\]^_`{|}啊"
    SYMBOL = string.ascii_letters + string.punctuation + "啊"
    length_symbol = len(SYMBOL)

    keyA, keyA_inverse = generateRandomKeys(length_symbol)

    cipher_text = multiplicative_cipher(keyA, length_symbol, plain_text)
    print(keyA, cipher_text)
    plain_text = multiplicative_cipher(keyA_inverse,length_symbol, cipher_text)
    print(keyA_inverse, plain_text)

