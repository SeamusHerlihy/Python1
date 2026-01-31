def sort_list(numbers):
    sorted_list = numbers.copy()

    for i in range(1, len(sorted_list)):
        current = sorted_list[i]
        j = i - 1

        while j >= 0 and sorted_list[j] > current:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1

        sorted_list[j + 1] = current

    return sorted_list


# Get user input
user_input = input("Enter numbers separated by commas: ")
numbers = list(map(int, user_input.split(",")))

# Sort and display result
sorted_numbers = sort_list(numbers)
print("Sorted list:", sorted_numbers)
