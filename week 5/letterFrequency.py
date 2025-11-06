import string

def basic_letter_counter(message):
    letter_counter = {x:0 for x in string.ascii_lowercase}
    for key,value in letter_counter.items():
        for chr in message.lower():
            if key is chr:
                letter_counter[key] += 1
    return letter_counter

def selection_sort(message):
    listed_message = list(message.items())
    for i in range(len(listed_message)-1):
        for j in range(i+1,len(listed_message)):
            if listed_message[i][1] < listed_message[j][1]:
                listed_message[i] , listed_message[j] = listed_message[j] , listed_message[i]
    return listed_message

def main():
    message = """this is a heads up to the ict students, 
    the exam will be very hard and they have to study so they would not fail 
    and stay as first year students and graduate after their kids"""
    print(selection_sort(basic_letter_counter(message)))

if __name__=="__main__":
    main()