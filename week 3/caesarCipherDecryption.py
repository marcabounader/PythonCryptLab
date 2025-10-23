import caesarCipher
import utils

cipher_text = caesarCipher.encrypt()
key = utils.key
SYMBOLS = utils.SYMBOLS
plain_text = ""

for chr in cipher_text:
    index = SYMBOLS.find(chr)
    if index != -1:
        shift = (index - key) % len(SYMBOLS)
        plain_text += SYMBOLS[shift]
    else:
        plain_text += chr

print(plain_text)