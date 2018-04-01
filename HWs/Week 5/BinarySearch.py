ls = [1,2,5,7,10,20]

# Find index of value
def findVal(target):
    left, right = 0, len(ls) - 1
    while left < right:
        # The middle is equal to the center of right and mid
        mid = (left+right) / 2
        # Check the current middle value
        if (ls[mid] == target):
            return mid
        # if the middle value is not equal to the target
        #Move the middle size of the array accordingly
        if (ls[mid] > target):
            right = mid
        else:
            left = mid
    return False

test1 = findVal(5)
if test1 == 2:
    print "Finished!"