def get_single_letter():
    while True:
        char = input("Enter a single character: ")
        if len(char) != 1:
            print("Error: Please enter exactly one character.")
        elif not char.isalpha():
            print("Error: Input must be a letter (a-z or A-Z).")
        else:
            return char.lower()  # Convert to lowercase for easier checking

# Get valid character from user
letter = get_single_letter()

# Check if vowel or consonant
if letter in 'aeiou':
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")
