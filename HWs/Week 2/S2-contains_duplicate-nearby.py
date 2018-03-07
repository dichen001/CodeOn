"""
Given an array of integers and an integer k, find out whether there are
two distinct indices i and j in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.

example 0: given nums=[1,2,3], and whatever k is, always return False
example 1: given nums=[1,2,1], and k = (2,3,4,.... N), always return True.
           Because the two duplicates with indices 0 and 2, whose absolute difference is 2, <= k.
example 2: given nums=[1,2,1], and k = 0 or 1, always return False.
           Because the two duplicates with indices 0 and 2, whose absolute difference is 2, > k.

"""


def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    ### Please write your code inside ###
    "Hint: use dictionary"



    ### Please write your code inside ###



"""    
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
    test0 = ([1,1,1], 0, False)
    test1 = ([1,1,1], 1, True)
    test2 = ([1,1,1], 2, True)
    test3 = ([1,1,1], 3, True)
    test4 = ([0,1,2], 0, False)
    test5 = ([0,1,2], 1, False)
    test6 = ([0,1,1], 1, True)

    tests = [test0, test1, test2, test3, test4, test5, test6]
    for i, test in enumerate(tests):
            print "------------- Test " +str(i) + " -------------"
            print "-Test Input:"
            print test[0], test[1]
            print "-Expected Output:"
            print test[2]
            print "-Your Output:"
            o = containsNearbyDuplicate(test[0], test[1])
            print o
            assert o == test[2], "Wrong return. Please try again."
    print '\n**** Congratulations! You have passed all the tests! ****'
