text = input("Enter a string: ")

# Remove spaces and convert to lowercase for fair comparison
cleaned = text.replace(" ", "").lower()

is_palindrome = True
left = 0
right = len(cleaned) - 1

while left < right:
    if cleaned[left] != cleaned[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
