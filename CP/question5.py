'''Given a sorted array. Write functions using binary search to calculate following 
things:
. lower_bound(x) : index of first element which is greater or equal to x in the given 
array
. upper_bound(x): index of first element which is greater than x in the given array
. is_present(x): return true if x is present in the array else return false
'''

def lower_bound(array, x):
    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(array, x):
    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

def is_present(array, x):
    lower_bound_index = lower_bound(array, x)
    return lower_bound_index < len(array) and array[lower_bound_index] == x
