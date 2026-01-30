def is_palindrome(s):
    if len(s) <= 1:
        return True
    # Check if the first and last characters are the same
    if s[0] != s[-1]:
        return False
    # Recursive call on the substring without the first and last characters
    return is_palindrome(s[1:-1])

# Prompt the user for input
user_input = input("Enter a string to check if it's a palindrome: ")
# Check and display the result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
