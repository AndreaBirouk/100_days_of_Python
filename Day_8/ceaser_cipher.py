import string

alphabet = list(string.ascii_lowercase)
characters = list(string.punctuation)

# print(alphabet)


def get_message(text, shift, direction):
    output_text = ''
    
    for letter in text:
        if letter in alphabet and direction == 'encode':
            output_text += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
        elif letter in alphabet and direction == 'decode':
            output_text += alphabet[alphabet.index(letter) - shift]
        else:
            output_text += letter
                
    print(f"Here is the {direction}d result: {output_text} \n")

should_continue= True

while should_continue:     

    direction = input('Type "encode" to encrypt, type "decode" to decrypt: \n').lower()
    text = input("Type your message: \n").lower()
    shift= int(input("Type the shift number: \n"))
    get_message(text, shift, direction)

    answer = input('Type "yes" if you want to go again. Otherwise type "no" \n').lower()

    if answer == 'no':
        should_continue = False
        print("Goodbye")



# def encrypt(text, shift):
#     encrypted_text = ''

#     for letter in text:
#         if letter in alphabet:
#             encrypted_text += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
#         elif letter == ' ':
#             encrypted_text += ' '
#         elif letter in characters:
#             encrypted_text += letter
#         else:
#             encrypted_text += letter
#     print(f"Here is the encoded result: {encrypted_text}")

# '''
# --> wrapped indexing: way to wrap the alphabet around is the modulo operator
# e.g. alphabet[30%len(alphabet)]'''



# def decrypt(text, shift):
#     decrypted_text = ''

#     for letter in text:
#         if letter in alphabet:
#             decrypted_text += alphabet[alphabet.index(letter) - shift]
#         elif letter == ' ':
#             decrypted_text += ' '
#         elif letter in characters:
#             decrypted_text += letter
#         else:
#             decrypted_text += letter
    
#     print(f"Here is the decoded result: {decrypted_text}")