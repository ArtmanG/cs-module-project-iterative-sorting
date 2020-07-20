# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) -1):
        # current index of the array we are looping
        cur_index = i
        # the smallest value array is whatever the current index is
        smallest_value = arr[cur_index]
        # the index of the smallest value is the current index
        smallest_index = cur_index
        # on the unsorted side of the array, loop through everything
        for unsorted_index in range(cur_index, len(arr)):
            # is the value of an unsorted index less than the current smallest value
            if arr[unsorted_index] < smallest_value:
                # set the variable smallest value to the new smallest value
                smallest_value = arr[unsorted_index]
                # set the the index smallest value to the new smallest value index
                smallest_index = unsorted_index
        # now that you've found a smaller value, you got to swap them
        # Example: cur_index = 7 smallest_index = 5  (7, 5 = 5, 7)
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # so we looped through all the numbers on this pass in the first for loop and made sure the index[0] is the smallest value, now we will do it again for the index[1] and make sure it is the next smallest value, and so on and so forth.
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Loop through your array
    # while swap = true
        # Compare each element to its neighbor
        # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
