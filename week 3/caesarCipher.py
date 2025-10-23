import utils

def main():
    SYMBOLS = utils.SYMBOLS
    plain_text = utils.plain_text
    cipher_text = ""
    key = utils.key

    for chr in plain_text:
        index = SYMBOLS.find(chr)
        if index != -1:
            shift = (index + key) % len(utils.SYMBOLS)
            cipher_text += SYMBOLS[shift]
        else:
            cipher_text += chr
    return cipher_text

if __name__ == "__main__":
    print(main())
