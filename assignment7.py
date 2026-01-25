# Prompt the user to enter a year
year_input = input("Enter a year: ")

# Check if the input is numeric
if not year_input.isdigit():
    print("Error: Please enter a valid numeric year.")
else:
    year = int(year_input)

    # Determine if it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
