# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
# greet_with_name('Emmy')

# def function_name(parameter):
#     # Do something. something = the argument
#     # Therefore parameter = the argumemnt
#     # Parameter is the name of the data being passed into the function
#     # Argument is the data being passed
    

# # Function with more than 1 parameter:
# def greet_with(name, location):
#     print(f"Hello {name}, from {location}!")
# greet_with('John', 'Nairobi') # This is called POSITIONAL ARGUMENT. Can't switch order of the arguments


# KEYWORD ARGUMENTS:
# Adds te arguments and parameter names in the function. def kwa(a=1, b=2, c=3):
# def greet_with(name='John', location='Nairobi'):
#     print(f"Hello {name} from {location}!")
# greet_with()
word_list = []
word = []
def split_words(sentence):
    for letter in sentence:
        while letter != ' ':
            word.append(letter)
            word = (f"{''.join(word)}")
            word_list.append(word)
        else:
            break
print(word_list)
print("Okay")
split_words("Hello World World Hello")
            