# Function to check if the given character is an alphabet
def is_alphabet(character):
    # Check if the character is an alphabet (either lowercase or uppercase)
    if character.isalpha():
        return True
    else:
        return False

# Input from user
char = input("Enter a character: ")

# Check if the character is a single character
if len(char) == 1:
    if is_alphabet(char):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
else:
    print("Please enter exactly one character.")
