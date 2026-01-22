def isalpha(char):
    return char.isalpha()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text, shift_key):
    ciper_text = ""
    for char in plain_text:
        if isalpha(char):
            shifted = ord(char) + shift_key
            if shifted > ord('z'):
                shifted -= 26
            ciper_text += chr(shifted)
        else:
            ciper_text += char
    print(f"Your encrypted message is: {ciper_text}")


def decryption(plain_text, shift_key):
    decrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shifted = ord(char) - shift_key
            if shifted < ord('a'):
                shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    print(f"Your decrypted message is: {decrypted_text}") 


what_to_do=input("Type 'encrypt, type 'decrypt' to decrypt:\n")
text=input("Type your message:\n").lower()  
shift=int(input("Type the shift number:\n"))

if what_to_do == 'encrypt':
    encryption(plain_text=text, shift_key=shift)
elif what_to_do == 'decrypt':
    decryption(plain_text=text, shift_key=shift)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {cipher_direction}d text is: {end_text}')
caesar(start_text=text, shift_amount=shift, cipher_direction=what_to_do)