"""
password = "1234"
if password == "1234":
    print("Access granted")
else:
    print("Access denied")


i=0
while i<5:
    print("Iteration", i)
    i +=1

#Reverse Cipher
message= "Hello, World!"
translates = ""
i = len(message)-1
while i>=0:
    translates+=message[i]
    i-=1
print(translates)
print(message[::-1])


name = "Rabih"

letter_a = name.find("a")

print(letter_a)
"""
#Ceaser Cipher
plain_text = "Hello World"
cipher_text= ""

key = 3
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

new_plain_text = plain_text.upper()
for letter in new_plain_text:
	if letter in LETTERS:
		number = LETTERS.find(letter)
		new_number = (number + key)% len(LETTERS)
		new_letter = LETTERS[new_number]
		cipher_text+= new_letter
	else:
		
		cipher_text+= new_letter

print(cipher_text)




