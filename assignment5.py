try:
    hours = float(input("Enter time duration in hours: "))

    if hours < 0:
        print("Time duration cannot be negative.")
    else:
        minutes = hours * 60
        seconds = hours * 3600

        print(f"\nTime in minutes: {minutes:.2f}")
        print(f"Time in seconds: {seconds:.2f}")

except ValueError:
    print("Invalid input. Please enter a numeric value for time.")
