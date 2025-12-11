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
    message = """Cryptography, the study of secure communication techniques that allow only the sender and intended recipient of a message to view its contents, is a field with a history stretching back millennia. The earliest known examples include the use of non-standard hieroglyphs in ancient Egypt and the famous Caesar cipher, attributed to Julius Caesar for protecting military communications. Throughout the Renaissance and into the modern era, complex mechanical and algorithmic systems were developed, escalating the arms race between code makers and code breakers. A major turning point arrived in the 20th century with the advent of computers, enabling algorithms like AES (Advanced Encryption Standard) and RSA, which form the foundation of modern digital security. Today, cryptography is not just about state secrets; it underpins the security of all internet transactions, from secure web browsing using HTTPS to the verifiable ledger technology of blockchain. Decrypting a message requires the correct key, which transforms the unintelligible ciphertext back into the original, readable plaintext, ensuring data integrity and confidentiality in an increasingly interconnected world."""
    SYMBOL = string.ascii_letters
    shuffled_list = [x for x in SYMBOL]
    random.shuffle(shuffled_list)
    key = ''.join(shuffled_list)
    translated_text = translate(key,SYMBOL,message)
    print(f"Encrypted:\n{translated_text}")
    print(f"Decryped:\n{translate(key,SYMBOL,translated_text,"decrypt")}")