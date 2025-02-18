import logging, math
from search import constants


def linearSearch(arr, value): # O(n)
    for i in range(len(arr)): 
        if arr[i] == value:
            return i
    return -1

def binarySearch(arr, value): # O(log2(n))
    l, r = 0, len(arr) - 1
    while(l <= r):
        mid = (l + r) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value: 
            r = mid - 1
        else: 
            l = mid + 1
    return -1

def ternarySearch(arr, value): # O(log3(n))
    l, r = 0, len(arr) - 1
    while l <= r:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3

        if arr[mid1] == value:
            return mid1
        elif arr[mid2] == value:
            return mid2
        elif value < arr[mid1]:
            r = mid1 - 1
        elif arr[mid2] < value:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1

    return -1

def jumpSearch(arr, value): # O(sqrt(n))
    n = len(arr)
    delta = math.sqrt(n)
    a, step = 0, delta
    while arr[int(min(step, n)) - 1] < value:
        a = step
        step += delta
        if a >= n:
            return -1

    step = int(step)
    a = int(a)
    while arr[a] < value:
        a += 1
        if a == min(step, n):
            return -1

    if arr[a] == value:
        return a    
    return -1
    

# There is another way to experimentally estimate the complexity of an algorithm
# This is by counting the elemental operations that the algorithm performs
# This could be a more precise way to estimate the complexity of an algorithm
# Take this function as an example for this approach    