"""
Algo

1. Linear (Sequential) Search - Runtime Analysis: Big O(n) 

Start with the first index:
    1. Chck if value at index = value we are searching for
        a. If YES:
            - Return index 
        b. If NO: 
            - If end of list reached, return item not found
            - else, index++ and repeat 
"""

def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1 # not found



"""
2. Binary Search - Runtime Analysis: Big O(log n) - you are skipping several indexes - not checking every single value

Start with the middle index:
    1. Chck if value at index = value we are searching for
        a. If YES:
            - Return index 
        b. If NO: 
            - if this was final index to search, return item not found
            - else, if value at index > target value, eliminarte RHS, repeat search on LHS
            - else, eliminate LHS, repeat search on RHS
"""

# Iterative 
# when we first get the list, we need to set 2 different pointers
def binary_searchI(my_list, search_item):
    # the first pointer low, will point to the first item in the list
    low = 0 # first index
    # The second pointer high, will point to the last item in the list
    high = len(my_list) -1 # last index
    
    # for each loop, we need to get the middle index
    # averaging the low pointer and high pointer (rounding down)
    while low <= high: # while loop
        # add the low pointer to the high pointer and divide by 2 (using the floor division operator //)
        middle = (low + high) // 2
        
        # set up a loop that will continue while the low pointer is less than or equal to the high pointer
        guess = my_list[middle]
        if guess == search_item:
            return middle # elimiate RHS
        if guess > search_item:
            high = middle - 1
        else: 
            low = middle + 1
    return None # not found

test_list = [2, 4, 7, 8, 9, 10, 12, 34, 45]
binary_searchI(test_list, 7)
binary_searchI(test_list, 34)


# Recursive
# Returns index of x in arr if present, else -1
def binary_searchR(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

