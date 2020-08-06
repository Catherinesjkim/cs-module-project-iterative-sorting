import sys

# TO-DO: Complete the selection_sort() function below - O(N^2)
def selection_sort(arr):
    # loop through n - 1 elements
    # start with current index = 0
    for i in range(0, len(arr) - 1):
        cur_index = i
        # loop through elements on right-hand-side of current index and find the smallest element
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)): 
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap the element at current index with the smallest element found in above loop
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# Driver code to test above
arr = [3, 1, 41, 59, 26, 53, 60, 62, 65, 34, 77, 98, 11]
print(arr)
selection_sort(arr)

# Let's see the list after we run the Selection Sort
print(arr)








# TO-DO: implement the Bubble Sort function below
# It's the simplest sorting algo that works by repeatedly swapping the adjacent elements if they are in wrong order
def bubble_sort(arr):
    # loop through your array - traverse through all array elements 
    for i in range(1, len(arr)): 
        
        # Last i elements are already in place
        for j in range(len(arr) - 1):
            
            # compare each element to its neighbor
            # traverse the array from 0 to n-i-1
            # swap if the element found is greater than the next element
            # if element in wrong position (relative to each other, swap them)
            if arr[j] > arr[j+1]:
                # Swap 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        # if no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1
    return arr

# Driver code to test above 
arr = [19, 13, 6, 2, 18, 8]
bubble_sort(arr)
# print(arr)


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
