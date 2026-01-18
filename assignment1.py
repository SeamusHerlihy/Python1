def calculate_simple_interest():
    try:
        # Input
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the interest rate (in %): "))
        time = float(input("Enter the time period (in years): "))

        # Validation for negative values
        if principal < 0 or rate < 0 or time < 0:
            print("Error: Principal, rate, and time must be non-negative numbers.")
            return

        # Processing
        simple_interest = (principal * rate * time) / 100

        # Output
        print(f"Simple Interest = {simple_interest}")

    except ValueError:
        print("Error: Please enter valid numeric values for principal, rate, and time.")


# Run the program
calculate_simple_interest()
