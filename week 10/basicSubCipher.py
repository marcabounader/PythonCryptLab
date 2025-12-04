import string
import random

def translate(key, SYMBOL, message, mode="encrypt"):
    translated = ''
    if mode == "decrypt":
        key , SYMBOL = SYMBOL, key
    for chr in message:
        index = SYMBOL.find(chr)
        if index != -1:
            translated += key[index]
        else:
            translated +=chr
    return translated


if __name__ == "__main__":
    message = input("Please enter the message to encrypt:\n")
    SYMBOL = string.ascii_letters
    shuffled_list = [x for x in SYMBOL]
    random.shuffle(shuffled_list)
    key = ''.join(shuffled_list)
    translated_text = translate(key,SYMBOL,message)
    print(f"Encrypted:\n{translated_text}")
    print(f"Decryped:\n{translate(key,SYMBOL,translated_text,"decrypt")}")