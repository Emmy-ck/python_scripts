# TO DO1: Create a functon called encrypt that takes the 'text' and 'shift' as inputs
# TO DO2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# TO DO3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
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
encrypt(word=text, encr=shift)

# DONE!
# Another solution:

# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# # In Angela's solution to avoid the list out of index error
# # the items were copied and manually appended to the initial list
# # In my code, I used built-in list methods to solve this error
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# text = list(text.strip(''))
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is: {cipher_text}")
# encrypt(plain_text=text, shift_amount=shift)