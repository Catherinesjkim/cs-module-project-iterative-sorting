"""
Big O Notation
- Worst Case complexity - rate of change - don't care about time (depends on the computer, etc.)
- N is the input size/variable that affects the number of steps/operations

Classifications

1. Constant Time Complexity - O(1): No matter of the size of your input, the steps/ops will be the same

2. Logarithmic Time - Log(N): How many times do you need to multiply 2 by itself to get 8? 2^3 = 8; log 8 = 3 (you can divide 8 by 2 with three times). Cutting our number in a half - BST.

3. Linear Time - O(N): When your input doubles, your time is half of your input. Search through unsorted data.

4. Linearithmic/Log-Linear - O(N * Log N): 

5. Polynomial Time - O(N^c): c == constant; quadratic, etc. 

6. Exponential Time - O(c^N): exponent is the size of the input, so that's why it's called exponential. For permutation, combinations, recursion

7. Factorial Time - O(N!): For permutation, combinations, recursion

"""

# Constant Time O(1) - Only one operation - runtime is Not dependent on n
def print_num(n): # will run very quickly
    print(n)

# Constant Time O(10000) - still only 10000 times no matter what's n
def print_num_10000(n):
    for _ in range(10000):
        print(n)

# Linear Time - would runtime dependent on n? yes
# O(n)
# n = 10
# n will be printed 10 times
# n = 10000000
# n will be printed 10000000 times
def print_num_n_times(n):
    for _ in range(n): # loop runs O(n) times
        print(n) # O(1)
       
# O(N*10000)
def print_num_n_times_modified(n):
    for _ in range(n): # loop runs O(n) times
        print(n)  # O(1)
        for _ in range(10000): # O(10000)
            print(n)
         
            
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear', 'Dog']

# Polynomial Time - size of the animals in relations to the steps needed to be taken - Non-Lineal
# (N * N) = O(N^2) - N square
def print_animal_pairs():  # triple for loops
    for animal_1 in animals:  # O(N)
        for animal_2 in animals:  # O(N)
                print(f'{animal_1} and {animal_2}')  # O(1)

print_animal_pairs()

# (N * N * N) = O(N^3) - N cubed
def print_animal_triplets(): # triple for loops
    for animal_1 in animals:  # O(N)
        for animal_2 in animals: # O(N)
            for animal_3 in animals:  # O(N)
                print(f'{animal_1} and {animal_2} and {animal_3}') #O(1)

print_animal_triplets()

# Logarithmic Time - O(log N) - holy grail of most algos to strive for - 3 steps instead of 100000 times
# Dividing of an input - shorten to half of our list of animals - dividing force in relation to n
# we are removing HALF of the remaining animals each time - by variable number
# the input gets reduced by a factor each iteration
def free_animals(animals):
    while len(animals) > 0:
        # : splice notation
        animals = animals[0: len(animals // 2)]


