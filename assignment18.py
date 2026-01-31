def concat_tuples(tuple1, tuple2):
    return tuple1 + tuple2


# Get tuples from the user
tuple1 = tuple(input("Enter the first tuple (comma-separated): ").split(","))
tuple2 = tuple(input("Enter the second tuple (comma-separated): ").split(","))

# Concatenate and display result
result = concat_tuples(tuple1, tuple2)
print("Concatenated tuple:", result)
