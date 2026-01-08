import string
SYMBOL = string.ascii_uppercase

def translate_message(key,message,mode):
    translated = []
    length_symbol = len(SYMBOL)
    index_key = 0
    length_key = len(key)
    for chr in message:

        if index_key == length_key:
            index_key = 0 
        index = SYMBOL.find(chr.upper())
        index_key_symbol = SYMBOL.find(key[index_key].upper())
        if index_key != -1 and index_key_symbol != -1:
            if mode == "encrypt":
                shift_index = (index + index_key_symbol) % length_symbol
            elif mode == "decrypt":
                shift_index = (index - index_key_symbol) % length_symbol
            translated.append(SYMBOL[shift_index] if chr.isupper() else SYMBOL[shift_index].lower())
        else:
            translated.append(chr)
        index_key += 1
    return ''.join(translated)

def main():
    message = input("Please enter the message to translate:")
    key = "LEMON"
    mode = input("decrypt or encrypt?")
    if mode == "encrypt" or mode == "e" or mode == "decrypt" or mode =="d":
        print(translate_message(key,message,mode))
    else:
        main()

if __name__ == "__main__":
    main()