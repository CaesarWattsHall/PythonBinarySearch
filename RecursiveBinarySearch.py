# Recursive binary search in python
def binary_search_recursive(array, x, low, high):
    # Base case: low and high pointers meet
    if low > high:
        return -1 # Not found the target value

    # Find the middle index
    mid = (low + high) // 2

    # Compare the middle element with the target value
    if array[mid] == x:
        return mid # Found the target value
    elif array[mid] < x:
        return binary_search_recursive(array, x, mid + 1, high) # Search in the right half
    else:
        return binary_search_recursive(array, x, low, mid - 1) # Search in the left half
