def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2
        return result

# Prompt user for input
try:
    base = int(input("Enter the base (integer): "))
    exponent = int(input("Enter the exponent (integer): "))
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")
except ValueError:
    print("Please enter valid integers for base and exponent.")
