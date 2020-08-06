# Similar to Uno card game - shuffling cards in my hand - swapping positions

# my_list = [8, 2, 5, 4, 1, 3]

# my_list = [8, | 2, 5, 4, 1, 3]

# temp = 2
# my_list = [2, 8, | 5, 4, 1, 3]

# temp = 5
# my_list = [2, 5, 8, | 4, 1, 3]

# temp = 4
# my_list = [2, 4, 5, | 8, 1, 3]

"""
[8, 2, 5, 4, 1, 3]
^
[2, 5, 4, 1, 3] < [8]
^
[1] < [2] > [5, 4, 3][8]
^
[1][2][4, 3] < [5] > [8]
^
[1][2][3] < [4] > [5][8]

"""

# Worst Time: O(N^2) - N square algo (2 loops)
# loops or recursion? Iterative solution - for loop & while loop (2 indices)
def insertion_sort(list_to_sort):
    # the first element is already in the "sorted side"
    # (abstract ide, no code required for the first line)
    
    # potential to run N times
    # for all other itmes, we should do things
    # starting at the second item (index 1), iterate until the end of the array - moving J here
    for i in range(1, len(list_to_sort)): # - it behaves like a linear loop
        # the current number at the index represents the value currently being Sorted
        current_num = list_to_sort[i]
        # move the current number back through the array (to the "sorted side")
        j = i # j is equal to the end of the array
        # keep moving j until (while loop - T or F): it's greater than the number before it OR we reach the start of the Array
        
        # potential to run N times - it behaves like a linear loop
        while j > 0 and current_num > list_to_sort[j-1]: # it can move all the way to the start
            # replace the current value with the one to the left of it - shifting that value over
            list_to_sort[j] = list_to_sort[j-1] 
            j -= 1 # decrement j as we go
        # set the value at the current index to the current number
        # at this moment, J represent the new location for the current number
        list_to_sort[j] = current_num
       
    return list_to_sort

print(insertion_sort([8, 4, 2, 5, 1, 3]))
