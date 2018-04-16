# Find a value with Binary search
def findVal(ls, target):
    # Opposite sides of the array
    left = 0
    right = len(ls)
    while left < right:
        mid = (left + right) / 2
        val = ls[mid]
        # Conditions
        if target == val:
            # The value we are looking for is in the middle
            return mid
        if target > val:
            # The value is on the greater side of the middle
            # Move the left side up to increase the middle
            left = mid
        if target < val:
            # The value is on the smaller side of the middle
            # Mode the right side down to decrease the middle
            right = mid