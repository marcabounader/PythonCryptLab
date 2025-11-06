import caesarCipherUtil
import utils
import detectEnglish
plain_text = "hello this is a secret text"
initial_key = 3

cipher_text = caesarCipherUtil.encrypt(initial_key,utils.SYMBOLS,plain_text)

for key in range(len(utils.SYMBOLS)):
    plain_text = caesarCipherUtil.decrypt(key,utils.SYMBOLS,cipher_text)
    if detectEnglish.is_english(plain_text):
        print(key,":",plain_text)
