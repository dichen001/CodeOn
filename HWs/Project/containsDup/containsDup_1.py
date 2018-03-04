"""
Question:

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example:

Given nums = [3,1,2,3],

Your function should return True, because 3 appears in nums[0] and nums[3].
"""


def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ### Please write your code inside ###

        list_nums = list(nums)
        set_nums = list(set(nums))
        rep_counter = 0

        # O(n)
        for set_value in set_nums:
            rep_counter = 0
            # O(n)
            for list_value in list_nums:
                if (list_value == set_value):
                    rep_counter+= 1

            if (rep_counter > 1):
                return True
        #Total: O(n^2)


        return False







        ### Please write your code inside ###




"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([1,1,1,1], True)
        test1 = ([3,1,2,3], True)
        test2 = ([1,3,2], False)
        test3 = ([], False)
        tests = [test0, test1, test2, test3]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0]
                print "-Expected Output:"
                print test[1]
                print "-Your Output:"
                print containsDuplicate(test[0])
                assert containsDuplicate(test[0]) == test[1], "Wrong return. Please try again."
                print '\n**** Congratulations! You have passed all the tests! ****'
