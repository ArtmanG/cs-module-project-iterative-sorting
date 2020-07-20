### Linear Search ###
# return the index of the target if it is in the array.
def linear_search(arr, target):
    if target in arr:
        return arr.index(target)

    return -1   # not found

### Binary Search ###
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    high = len(arr)
    low = 0
    mid = (high + low) // 2

    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search(arr, target), mid -1
    elif arr[mid] < target:
        return binary_search(arr, target), mid +1

    else:
        return -1  # not found
