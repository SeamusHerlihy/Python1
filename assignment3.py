try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
    else:
        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 25:
            print("Category: Normal weight")
        elif 25 <= bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Invalid input. Please enter numeric values for weight and height.")
