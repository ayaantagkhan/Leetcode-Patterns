def binary_search(items, target):
    ## Good for locating a single element
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] <= target:
            left = mid + 1 
        else:
            right = mid - 1

    return -1 

def two_pointers(items, target):
    ## Good for tracking intervals or comparing elements
    left = 0
    right = len(items) - 1

    while left < right:
        total = items[left] + items[right]

        if total == target:
            return left, right
        elif total < target:
            left = left + 1
        else: 
            right = right - 1
    return None

