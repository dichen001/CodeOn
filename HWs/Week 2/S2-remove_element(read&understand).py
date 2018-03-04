"""
Question:

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""

"""
### Please read and understand my code below. (Modified from your code.)
### Note that we previously sort the list first, which is O(N*log(N)) for merely using the sort() alone.
### Now the running complexity is changed to O(N)
### Also note that our previous implementation won's pass the newly added test4 and test5.
"""

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    end_index = -1
    n = len(nums)
    # Think about why I add this loop using the example <nums=[2,3,2], val=2>
    while n + end_index >= 0 and nums[end_index] == val:
        end_index -= 1
    current_index = 0
    while (current_index < len(nums) + end_index):
        if (nums[current_index] == val):
            # Swap values from current and end index
            nums[current_index], nums[end_index] = nums[end_index], nums[current_index]
            # Update current and end values
            current_index += 1
            end_index -= 1
        else:
            current_index += 1
    # if current pointer is not in the start of "trash zone",
    # i.e. it's still in the end of the "valid zone", we return the length of the "valid zone".
    # Think about why I add the follow if statement using the example <nums=[2,3,3], val=3>
    if current_index < n and nums[current_index] != val:
        return current_index + 1
    else:
        return current_index



"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
    test0 = ([], 1, 0)
    test1 = ([2, 3, 2], 2, 1)
    test2 = ([2, 3, 2], 3, 2)
    test3 = ([2, 3, 3, 1, 2, 2], 2, 3)
    test4 = ([2, 3, 3, 1, 2, 2], 1, 5)
    test5 = ([2, 3, 3, 1, 2, 2], 3, 4)
    tests = [test0, test1, test2, test3, test4, test5]
    for i, test in enumerate(tests):
        print "------------- Test " + str(i) + " -------------"
        print "-Test Input:"
        print test[0:2]
        print "-Expected Output:"
        print test[2]
        print "-Your Output:"
        print removeElement(test[0], test[1])
        assert removeElement(test[0], test[1]) == test[2], "Wrong return. Please try again."
    print '\n**** Congratulations! You have passed all the tests! ****'
