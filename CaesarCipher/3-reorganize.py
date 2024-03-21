# TO DO 1: COmbine the encrypt() and decrypt() functions into a single function called caesar().
# TO DO 2: Call the caesar() functon passing over the 'text', 'shift' and 'direction' values
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
text = list(text.strip(''))
shift = int(input("Type the shift number:\n"))

def caesar(word=text, num=shift, dir=direction):
    if dir == 'encode':
        encrypt_word = []
        for let in word:
            x = int(alphabet.index(let)) + num
            if x > alphabet.index(alphabet[-1]): # CHecks whether the new index is out of range from the alphabet list
                extra = (f"{''.join(alphabet)}") # Combined the list to a string
                extra = list(extra.strip('')) # Splits the combined string to individual items t add to the list
                for l in extra:
                    alphabet.append(l) # Appends eah item to the list to extend the list
            encrypt_word.append(alphabet[x])
        print(f"The encoded text is: {''.join(encrypt_word)}")
    
    elif dir == 'decode':
        decrypt_word = []
        extra = (f"{''.join(alphabet)}") # Combined the list to a string
        extra = list(extra.strip('')) # Splits the combined string to individual items t add to the list
        for l in extra:
            alphabet.append(l)
        alphabet.reverse()
        for let in word:
            x = int(alphabet.index(let)) + num
            decrypt_word.append(alphabet[x])
        print(f"The decoded text is: {''.join(decrypt_word)}")
caesar(word=text, num=shift, dir=direction)

# DONE in record time
# Angela's solution:
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# # In Angela's solution to avoid the list out of index error
# # the items were copied and manually appended to the initial list
# # In my code, I used built-in list methods to solve this error
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def caesar(start_text, shift_amount, cipher_direction) :
#     end_text = ""
#     if cipher_direction == 'decode':
#         shift_amount *= -1
#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"The {cipher_direction}d text is {end_text}")
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
