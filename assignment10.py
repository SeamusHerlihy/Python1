def get_positive_age():
    while True:
        age_input = input("Enter your age: ")
        try:
            age = int(age_input)
            if age > 0:
                return age
            else:
                print("Error: Age must be a positive integer. Try again.")
        except ValueError:
            print("Error: Please enter a valid integer for age.")

# Get valid age from user
age = get_positive_age()

# Classify age
if age < 18:
    category = "Minor"
elif age <= 65:
    category = "Adult"
else:
    category = "Senior citizen"

# Display result
print(f"Your age category is: {category}")
