


def binary_search(arr, low, high, x):
    """return the index of the element searched"""
    mid = 0
    high = len(arr) - 1

    for element in range(0, (len(arr) - 1 /2)):

        if high >= low:
    
            mid = (high + low) // 2
    
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
    
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                mid = mid - 1

            # Else the element can only be present in right subarray
            else:
                mid = mid + 1
    
        else:
            # Element is not present in the array
            return -1
