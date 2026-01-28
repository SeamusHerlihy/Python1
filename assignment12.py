while True:
    try:
        rows = int(input("Enter the number of rows: "))
        if rows <= 0:
            print("Please enter a positive integer for rows.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

char = input("Enter the character to use for the pattern: ")

print("\nRight Triangle Pattern:\n")
for i in range(1, rows + 1):
    for j in range(i):
        print(char, end=" ")
    print()
