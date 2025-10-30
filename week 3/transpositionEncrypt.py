import random
from math import ceil
import sys
plain_text = "I love abbas, but abbas doesn't love me"
key = col = 4
cipher_text = ""
row = ceil(len(plain_text) / key)

def encrypt():
    global cipher_text
    pointer = 0
    counter = 0
    while pointer < len(plain_text):
        col = 0
        if (col ==(key-1) and (pointer < (row*key-len(plain_text)-row))):
            break
        cipher_text += cipher_text[pointer]
        pointer += key
        if counter == row - 1:
            break
        if(pointer >= row and pointer != len(plain_text)-1 ):
            pointer += 1
            col += 1
            counter = 0
    print(cipher_text)
    
if __name__ == "__main__":
    encrypt()