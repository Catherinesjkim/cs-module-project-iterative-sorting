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
# print(f'Element found at index ' + str(linear_search(arr, target)))


# Write an iterative implementation of Binary Search
# It returns index of target in given array arr if present,
# else returns -1
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    middle = 0
    
    while low <= high:
        middle = (high + low) // 2
        
        # check if target is present at middle
        if arr[middle] < target:
            low = middle + 1
            
        # if target is greater, ignore left half
        elif arr[middle] > target:
            high = middle - 1
            
        # if target is smaller, ignore right half
        else:
            return middle
        
    # if we reach here, then the element was not present
    return -1  # not found

# Test array 
arr = [2, 3, 4, 10, 40]
target = 10

# Function call
result = binary_search(arr, target)
print(f'Element found at index ' + str(binary_search(arr, target)))
