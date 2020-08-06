import random
import time # We'll use this later 

my_range = 50000000000
my_size = 100000 # random size of numbers to output

random_nums = random.sample(range(my_range), my_size)

# print(random_nums)
num_to_find = 4578 # target number

# O(N) linear time
def linear_search(arr, target):
    # loop through the array one item at a time, 
    for num in arr:
        # check each value if it matches target, return True
        if num == target:
            return True
    # otherwise, return False
    return False

print("Linear")
start = time.time()
print(linear_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")


# BST - Logarithmic - O(log n) because we are halving the input all the time
random_nums = [4, 10, 13, 17, 21, 26, 29, 31, 32, 50, 67, 70, 74, 85, 92] # array
# sorted data set - BST is only faster if the data is sorted
def binary_search(arr, target):
    # beginning of the window/array
    start = 0
    # end of the window/array
    end = (len(arr) - 1)
    
    found = False # to keep track of the while loop - boolean
    while end >= start and not found: # the target
        # then find the middle index of our array = start + end // 2 
        middle_index = (start + end) // 2 # use floor division so that you don't get a float
        
        # compare the value in the middle with target
        # if the middle value is the same as target, set found variable to True
        if arr[middle_index] == target:
            found = True
            
        else: # move start or end index closer to one another, and shrink our search space
            # if the value is not equal & larger to the target,
            if target < arr[middle_index]:
                end = middle_index - 1 # move to 1 before the median
                
            # if the value is not equal & smaller to the target,
            if target > arr[middle_index]:
                start = middle_index + 1 # then move 1 after the median
    return found

print("Binary")
start = time.time()
random_nums.sort()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")

print("Binary")
start = time.time()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")
