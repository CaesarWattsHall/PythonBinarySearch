# Iterative binary search in python
def binary_search_iterative(array, x):
    # Initialize low and high pointers
    low = 0
    high = len(array) - 1

    # Repeat until low and high meet
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Compare the middle element with the target value
        if array[mid] == x:
            return mid # Found the target value
        elif array[mid] < x:
            low = mid + 1 # Search in the right half
        else:
            high = mid - 1 # Search in the left half

    return -1 # Not found the target value
