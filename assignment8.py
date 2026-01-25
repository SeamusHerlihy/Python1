def get_valid_mark(subject):
    while True:
        mark_input = input(f"Enter marks for {subject} (0-100): ")
        try:
            mark = float(mark_input)
            if 0 <= mark <= 100:
                return mark
            else:
                print("Error: Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Error: Please enter a numeric value. Try again.")

# Get marks for three subjects
mark1 = get_valid_mark("Math")
mark2 = get_valid_mark("Science")
mark3 = get_valid_mark("English")

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display result
print(f"Average marks: {average:.2f}")
print(f"Grade: {grade}")
