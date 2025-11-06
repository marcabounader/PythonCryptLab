def decrypt(key,SYMBOLS,cipher_text):
    plain_text = ""
    for chr in cipher_text:
        index = SYMBOLS.find(chr)
        if index != -1:
            shift = (index - key) % len(SYMBOLS)
            plain_text += SYMBOLS[shift]
        else:
            plain_text += chr
    return plain_text

def encrypt(key,SYMBOLS,plain_text):
    cipher_text = ""

    for chr in plain_text:
        index = SYMBOLS.find(chr)
        if index != -1:
            shift = (index + key) % len(SYMBOLS)
            cipher_text += SYMBOLS[shift]
        else:
            cipher_text += chr
    return cipher_text