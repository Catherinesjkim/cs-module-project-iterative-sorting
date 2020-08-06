# Algo

An algo is a set of instructions for accomplishing a task. We could call every piece of code an algo. 
Choose the most efficient algo (considering both time and space efficiency depending on our needs).

1 Linear (Sequential) Search - Big Linear O(n)

Start with the first index:
    1. Chck if value at index = value we are searching for
        a. If YES:
            - Return index 
        b. If NO: 
            - If end of list reached, return item not found
            - else, index++ and repeat 


2 Binary Search - Big Logarithmic O(log n)

Start with the middle index:
    1. Chck if value at index = value we are searching for
        a. If YES:
            - Return index 
        b. If NO: 
            - if this was final index to search, return item not found
            - else, if value at index > target value, eliminarte RHS, repeat search on LHS
            - else, eliminate LHS, repeat search on RHS

## TYPES OF SORTING ALGO

Insertion, Selection, and Bubble Sort are iterative algos that we can use to order items in a data structure. How do these algos scale & will it work with big numbers?

1 Insertion Sort - Sorted Array to Balanced BST (GeeksforGeeks)

    Best case: O(n) - already sorted. I will still have to go through each item in the collection to make sure it's in the correct position. 

    Worst & Average cases: O(n^2) - if the collection is sorted in decreasing order. Maximum number of iterations to shift items to the right.

Holding n cards in my hand:

- consider the first card a "sorted" array of length 1
- start with the second card and insert it into the "sorted" part of the array
- repeat the previous step with the next card until all cards in the "sorted" subarray 


2 Selection Sort

    a. Out-of-place selection sort: there's enough space to start a new collection
    b. In-place selection sort: There's no space to start a new collection, swap books as we encounter them

Holding n cards in my hand:

- first select the smallest card and move it to the far left
- then select the next smallest card and move it to the left so that it is to the immediate right of the previous card 


3 Bubble Sort - simplest and very ineficient

    Best case: O(n) - Only the outer loop runs
    Worst case: O(n^2) - The inner loop has to perform 1/2 * n operations due to swapping every element.

Holding n cards in my hand:

- Only compare the direct neighbors - first pair of elements 
    - if the RHS is less than the LHS, swap 
    - else, do nothing 
- iterate through the array, compraing other pairs of adjacent elements 
- if 1 or more swaps performed, repeat above process


4 Merge Sort - Big Linearithmic O(n log n)

