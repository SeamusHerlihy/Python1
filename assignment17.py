def find_common_elements(list1, list2):
    set1 = set(list1)
    common_elements = []

    for item in list2:
        if item in set1:
            common_elements.append(item)

    return common_elements

list1 = input("Enter the first list (comma-separated): ").split(",")
list2 = input("Enter the second list (comma-separated): ").split(",")

list1 = [item.strip() for item in list1]
list2 = [item.strip() for item in list2]

result = find_common_elements(list1, list2)
print("Common elements:", result)
