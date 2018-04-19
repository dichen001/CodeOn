"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0

"""

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ### Please start your code here###



    ### End ###

"""

Below are the test cases I created for testing the correctness of your code.
Please don't modify them when you push the file back to GitHub
"""

if __name__ == '__main__':
        test0 = ([], 1, 0)
        test1 = ([1,3,5,6], 5, 2)
        test2 = ([1,3,5,6], 2, 1)
        test3 = ([1,3,5,6], 7, 4)
        test4 = ([1,3,5,6], 0, 0)
        tests = [test0, test1, test2, test3, test4]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0]
                print "-Expected Output:"
                print test[1]
                print "-Your Output:"
                your_ans = searchInsert(test[0], test[1])
                print your_ans
                assert your_ans == test[2], "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'
