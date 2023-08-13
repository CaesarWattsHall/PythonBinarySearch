# PythonBinarySearch
 Binary search is a search algorithm that finds the position of a target value in a sorted list by repeatedly dividing the list into two halves and comparing the middle element with the target value. Binary search can be implemented in Python both iteratively and recursively.

To use these functions, you need to pass a sorted list as the first argument, the target value as the second argument, and optionally the low and high indices as the third and fourth arguments for the recursive function.

# TimeComplexity
The time complexity of binary search is a measure of how fast the algorithm can find the position of a target value in a sorted list. The time complexity depends on how many comparisons the algorithm needs to make before finding the target value or concluding that it is not in the list.

The best case time complexity of binary search is **O(1)**, which means that the algorithm only needs one comparison to find the target value. This happens when the target value is exactly at the middle of the list, which is the first element that the algorithm compares.

The average case and the worst case time complexity of binary search are both **O(log N)**, where **N** is the number of elements in the list. This means that the algorithm needs at most **log N** comparisons to find the target value or conclude that it is not in the list. This happens when the target value is either at one of the ends of the list or not in the list at all, which requires the algorithm to divide the list into two halves repeatedly until there is only one element left.

The space complexity of binary search is **O(1)**, which means that the algorithm does not use any extra space to store intermediate results. The algorithm only needs a few variables to keep track of the low, high, and mid indices of the search space.
