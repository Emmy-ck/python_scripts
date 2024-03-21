# TO DO1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs
# TO DO2: Inside the 'decrypt' function, shift each letter of the 'text' backwards in the alohabet by the shift amount and print the decrypted text
# TO DO3: Check if the user wanted to enncrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that direction variable. You should be able to test the code to encrypt and decrypt a message
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
text = list(text.strip(''))
shift = int(input("Type the shift number:\n"))

encrypt_word = []
def encrypt(word=text, encr=shift):
    for let in word:
        x = int(alphabet.index(let)) + encr
        if x > alphabet.index(alphabet[-1]): # CHecks whether the new index is out of range from the alphabet list
            extra = (f"{''.join(alphabet)}") # Combined the list to a string
            extra = list(extra.strip('')) # Splits the combined string to individual items t add to the list
            for l in extra:
                alphabet.append(l) # Appends eah item to the list to extend the list
        encrypt_word.append(alphabet[x])
    print(f"The encoded text is: {''.join(encrypt_word)}")

decrypt_word = []
def decrypt(word=text, decr=shift) :
    extra = (f"{''.join(alphabet)}") # Combined the list to a string
    extra = list(extra.strip('')) # Splits the combined string to individual items t add to the list
    for l in extra:
        alphabet.append(l)
    alphabet.reverse()
    for let in word:
        x = int(alphabet.index(let)) + decr
        decrypt_word.append(alphabet[x])
    print(f"The decoded text is: {''.join(decrypt_word)}")

if direction == 'encode':
    encrypt(word=text,encr=shift)
else:
    decrypt(word=text,decr=shift)
    
# DONE in record time!
# Angela's solution:

# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# # In Angela's solution to avoid the list out of index error
# # the items were copied and manually appended to the initial list
# # In my code, I used built-in list methods to solve this error
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is: {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is: {plain_text}")

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)