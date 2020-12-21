import math

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    l = 0
    r = len(arr) - 1

    # has to be in order
    while l <= r:

        # define middle. floor returns whole number
        mid = math.floor((l + r) / 2)

        # if target present in the middle
        if arr[mid] == target:
            return mid

        # if target is greater than middle
        if arr[mid] < target:
            # move left barrier to right of middle
            l = mid + 1
        
        # if target is smaller than middle
        else:
            # move right barrier to left of middle
            r = mid -1

    # left no longer smaller than right- means target not present.
    return -1  # not found

