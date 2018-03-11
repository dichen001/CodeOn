"""
Given a list of multiple values, count the frequency of each value.
Return a dictionary, where the key is the value from the given list,
and the value is the frequency of the value shown in the given list.

Example:

Given nums = [3,2,2,3,1]
Your should return a dictionary like: {3:2, 2:2, 1:1}
"""

def getCounter(nums):
        """
        :type nums: List[int]
        :rtype: dict
        """
        ### Please write your code inside ###

        hash = {}

        # O(n)
        for num_val in nums:
            # If the number does not exist, add it to the list with
            # with a repeat value of 1
            # if (not hash.get(num_val, False)):
            if num_val not in hash:
                hash[num_val] = 1
            else:
                # If the number does exist, increment the value in the
                # Dictionary
                hash[num_val] += 1

        return hash


        ### Please write your code inside ###


"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
import random, collections

if __name__ == '__main__':
        test0 = [1,1,1,1]
        test1 = [3,1,2,3]
        test2 = [1,3,2]
        test3 = []
        test4 = [3,1,2,3,1,4,4,4]
        random.seed(666)
        test5 = [random.randint(1,10) for _ in range(50)]
        random.seed(777)
        test6 = [random.randint(1,20) for _ in range(1000)]
        tests = [test0, test1, test2, test3, test4, test5, test6]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test
                print "-Expected Output (Order & Type does not matter):"
                print dict(collections.Counter(test))
                print "-Your Output (Order & Type does not matter):"
                print getCounter(test)
                assert getCounter(test) == collections.Counter(test), "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'
