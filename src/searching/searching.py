### Linear Search ###
# return the index of the target if it is in the array.
def linear_search(arr, target):
    if target in arr:
        return arr.index(target)

    return -1   # not found

### Binary Search ###
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    high = len(arr) - 1
    low = 0
    

    while low <= high:
        mid = (high + low) // 2

        if target == arr[mid]:
            return mid

        if target < arr[mid]:
            high = mid - 1
        if target > arr[mid]:
            low = mid + 1
    return -1  # not found
