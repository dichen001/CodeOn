"""
Question:

Given an array of integers, find all the duplicates of the array.

Your function should return a list of all the value that appears at least twice in the array,
and it should return an empty list if every element is distinct.

Example:

Given nums = [3,1,2,3],

Your function should return [3], because 3 appears in nums[0] and nums[3].

Given nums = [1,2,3],

Your function should return [], because every element is distinct.

Given nums = [3,1,2,3,1,4,4,4],

Your function should return [3,1,4], because 3, 1 and 4 all appear more than once.

# note that the order does not matter.
"""

def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ### Please write your code inside ###








        ### Please write your code inside ###




"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([1,1,1,1], [1])
        test1 = ([3,1,2,3], [3])
        test2 = ([1,3,2], [])
        test3 = ([], [])
        test4 = ([3,1,2,3,1,4,4,4], [3,1,4])
        tests = [test0, test1, test2, test3, test4]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0]
                print "-Expected Output (Order does not matter):"
                print test[1]
                print "-Your Output:"
                print findDuplicate(test[0])
                assert set(findDuplicate(test[0])) == set(test[1]), "Wrong return. Please try again."
                print '\n**** Congratulations! You have passed all the tests! ****'
