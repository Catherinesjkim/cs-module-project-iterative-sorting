# The time complexity of above algorithm is O(n).
def linear_search(arr, target):
    # searching an element in a list/array in python can be simply done using \'in\' operator
    # lienearly search target in arr[]
    # start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    for i in range(len(arr)):
        # if target matches with an element, return the index
        if arr[i] == target:
            # return the index
            return i
        
    # if target doesn't match with any of elements, return -1
    return -1  # not found

# Driver code
arr = ['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
target = 'r'
print(f'Element found at index ' + str(linear_search(arr, target)))
















# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found
