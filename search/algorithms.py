import logging, math
from search import constants

def linearSearch(arr, value):
    for i in range(len(arr)):       # O(n) 
        if arr[i] == value:         # O(1)
            return i                # O(1)
    return -1                       # O(1)

# O(linearSearch) = (O(n) * O(1)) + O(1) + O(1) = O(n) 
# Worst Case: O(n) Iterates through the whole array
# Best Case: O(n) The value to search is the first one. 

# All the algorithms below need the array to be sorted

def binarySearch(arr, value):       # O(log2(n))
    l, r = 0, len(arr) - 1          # O(1)
    while(l <= r):                  # O(log2(n))
                                    # The amount of iterations will be log2(n) because the array is cut in 
                                    # halves
        mid = (l + r) // 2          # O(1)
        if arr[mid] == value:       # O(1)
            return mid              # O(1)
        elif arr[mid] > value:      # O(1)
            r = mid - 1             # O(1)
        else:                       # O(1)
            l = mid + 1             # O(1)
    return -1                       # O(1)

# O(binarySearch) = O(log2(n))
# Worst Case: O(log2(n)) The value to search is the first or last one or the element isn't present.
# Best Case: O(1) The value to search is found in the middle within the first iteration. 


def ternarySearch(arr, value):      # O(log3(n))
    l, r = 0, len(arr) - 1          # O(1)
    while l <= r:                   # O(log3(n))
                                    # The amount of iterations will be log2(n) because the array is cut in 
                                    # three parts and one of the blocks is chosen 
        mid1 = l + (r-l)//3         # O(1)
        mid2 = r - (r-l)//3         # O(1)

        if arr[mid1] == value:      # O(1)
            return mid1             # O(1)
        elif arr[mid2] == value:    # O(1)
            return mid2             # O(1)
        elif value < arr[mid1]:     # O(1)
            r = mid1 - 1            # O(1)
        elif arr[mid2] < value:     # O(1)
            l = mid2 + 1            # O(1)
        else:                       # O(1)
            l = mid1 + 1            # O(1)
            r = mid2 - 1            # O(1)

    return -1                       # O(1)

# O(ternarySearch) = O(log3(n))
# Worst Case: O(log3(n)) The value to search is the first or last one or the element isn't present.
# Best Case: O(1) The value to search is found within the mid values in the first iteration. 

def jumpSearch(arr, value): # O(√n)
    n = len(arr)                                # O(1)
    if n == 0:                                  # O(1)
        return -1                               # O(1)

    delta = math.sqrt(n)                        # O(1)
    a, step = 0, delta
    while arr[int(min(step, n)) - 1] < value:   # O(√n)
        a = step                                # O(1)
        step += delta                           # O(1)
        if a >= n:                              # O(1)
            return -1                           # O(1)

    step = int(step)                            # O(1)             
    a = int(a)                                  # O(1)
    while arr[a] < value:                       # O(√n)
        a += 1                                  # O(1)
        if a == min(step, n):                   # O(1)
            return -1                           # O(1)

    if arr[a] == value:                         # O(1)
        return a                                # O(1)
    return -1                                   # O(1)

# O(jumpSearch) = O(√n) + O(√n) = O(2√n) = O(√n)
# Worst Case: O(√n) The value to search is the last one or the element it's greater than the last value.
# Best Case: O(1) The value to search is the first element of the array. 