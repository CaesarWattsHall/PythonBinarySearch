# Example of using binary search functions

# A sorted list of numbers
array = [2, 4, 6, 8, 10, 12, 14]

# A target value to search for
x = 10

# Call the iterative function and print the result
result_iterative = binary_search_iterative(array, x)
print("Iterative result:", result_iterative)

# Call the recursive function and print the result
result_recursive = binary_search_recursive(array, x, 0, len(array) - 1)
print("Recursive result:", result_recursive)
