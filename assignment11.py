while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print("\nCollatz sequence:")
while num != 1:
    print(num, end=" -> ")
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1

print(1)
