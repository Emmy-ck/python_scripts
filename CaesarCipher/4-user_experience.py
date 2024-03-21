# TO DO1: Import and print the logo from art.py when the program starts
# TO DO4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g Type 'yes' if you want to go again. Otherwise, type 'no'
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again
# # Hint: Try create a new function that calls itself if the user types 'yes'
 # TO DO 2: What if the user enters a shift that is greater than the number of letters in the alphabet?
 # Try running the program and entering a shift number of 4.
 # Hint: Think about how you can use the modulus (%)
 
print("Caesar's Cipher Program")

def game():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    text = list(text.strip(''))
    shift = int(input("Type the shift number:\n"))
    
    def caesar(word=text, num=shift, dir=direction):
        if dir == 'encode':
            encrypt_word = []
            for let in word:
                if let in alphabet:
                    x = int(alphabet.index(let)) + num
                    if x > alphabet.index(alphabet[-1]): # Checks whether the new index is out of range from the alphabet list
                        x = x % (len(alphabet))
                        new_let = alphabet[x]
                elif not let in alphabet:
                    new_let = let
                encrypt_word.append(new_let)
            print(f"The encoded text is: {''.join(encrypt_word)}")
    
        elif dir == 'decode':
            decrypt_word = []
            alphabet.reverse()
            for let in word:
                if let in alphabet:
                    x = int(alphabet.index(let)) + num
                    if x > alphabet.index(alphabet[-1]):
                        x = x % len(alphabet)
                        new_let = alphabet[x]
                elif not let in alphabet:
                    new_let = let
                decrypt_word.append(new_let)
            print(f"The decoded text is: {''.join(decrypt_word)}")
    caesar(word=text, num=shift, dir=direction)
    option = input("Would you like to run again?\nType 'yes' to run again,type 'no' to quit: ")
    if option == "yes":
        game()
    else:
        print("Goodbye!")
game()

# DONE!!!
# Angela's solution:

## Copy from replit ##