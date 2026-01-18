# Fixed exchange rates
exchange_rates = {
    "USD to EUR": 0.92,
    "EUR to USD": 1.09,
    "USD to GBP": 0.79,
    "GBP to USD": 1.27
}

print("Available currency conversions:")
for key in exchange_rates:
    print("-", key)

try:
    choice = input("\nEnter a conversion pair exactly as shown above: ")

    if choice not in exchange_rates:
        print("Invalid currency pair selected.")
    else:
        amount = float(input("Enter the amount to convert: "))

        if amount < 0:
            print("Amount cannot be negative.")
        else:
            converted_amount = amount * exchange_rates[choice]
            target_currency = choice.split(" to ")[1]

            print(f"\nConverted amount: {converted_amount:.2f} {target_currency}")

except ValueError:
    print("Invalid input. Please enter a numeric amount.")
