text = 'Hello Zaira'
shift = 3

def caesar(message,offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char,1,10) # find method takes string, starting index and ending, last 2 are default none
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('Plain text:',message)
    print('Encrypted text:',encrypted_text)

caesar(text,shift)


""" REVISION
# caesar function takes two parameters message and offset
# function takes plane text and return encrypted text
# function contains alphabet string from a-z
# based on provided shift/Offset text is encrypted
import random
text = "Python is cool&$#"
shift = 4

def caesar(message,offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            index = alphabet.find(char.lower())
            new_index = (index + offset) % len(alphabet)
            new_char = alphabet[new_index]
            encrypted_text += new_char.upper() if is_upper else new_char
        else:
            if char == ' ':
                encrypted_text += char
            else:
                random_number = random.randint(1, 26)
                encrypted_text += alphabet[random_number]
    
    print("Plain text: ",message)
    print("Encrypted text: ",encrypted_text)

caesar(text,shift) """
