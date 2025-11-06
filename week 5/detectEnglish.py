import re

def load_dictionary():
    dictionary_content = open("dictionary.txt").readlines()
    return [x.strip().lower() for x in dictionary_content]

def detect_english(message):
    count = 0
    for word in message.lower().split():
        if word in load_dictionary():
            count += 1
    return (count / len(message.split())) * 100
def remove_non_letters(message):
    pattern = r"[^a-z\s]"
    clean_message = ""
    for word in message:
        for chr in word:
            if chr.isalpha() or chr == " ":
                clean_message += chr
    return re.sub(pattern, "", message)

def is_english(message, word_percentage = 20, letter_percentage = 80):
    clean_message = remove_non_letters(message)
    return (detect_english(message) >= word_percentage) and ((len(clean_message) / len(message))* 100) >= letter_percentage
def main():
    message = "this is an sentence written in english language by terminator66!!!!!!!!!"
    print("english" if is_english(message) else "no")

if __name__ == "__main__":
    main()