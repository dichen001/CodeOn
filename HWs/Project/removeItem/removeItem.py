"""
Question:

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""


def removeElement(nums, val):
    """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ### Please write your code inside ###
    l = len(nums)
    for i, n in enumerate(nums):
        if (n == val):
            nums.pop(i)
    o = len(nums)
    return o;
        ### Please write your code inside ###



# nums: [1,2,1]
# val: 1
# 0: nums.pop(0) --> [2,1]
# 1:
# 2: nums.pop(2)

# swap #
# a = 1
# b = 2
# a, b = b, a

"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
    test0 = ([2, 3, 2], 2, 1)
    test1 = ([2, 3, 2], 3, 2)
    test2 = ([2, 3, 3, 1, 2, 2], 2, 3)
    tests = [test0, test1, test2]
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
