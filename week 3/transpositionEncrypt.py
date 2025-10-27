import random

plain_text = "I love abbas, but abbas doesn't love me"
key = 4
cipher_text = ""
row = len(plain_text) // key 

def encrypt():
    global cipher_text
    pointer = 0
    while pointer < len(plain_text):
        cipher_text += cipher_text[pointer]
        pointer += key
        if (pointer ==(key-1) and (pointer < (row*key-len(plain_text)-row))):
            break
        if(pointer >= row and pointer != len(plain_text)-1 ):
            pointer += 1
    print(cipher_text)
    
if __name__ == "__main__":
    encrypt()