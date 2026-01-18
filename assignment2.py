def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive number greater than zero.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

# Input
length = get_positive_number("Enter the length of the rectangle: ")
width = get_positive_number("Enter the width of the rectangle: ")

# Processing
area = length * width

# Output
print(f"The area of the rectangle is: {area}")
