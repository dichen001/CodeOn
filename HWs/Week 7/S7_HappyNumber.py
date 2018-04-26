"""

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or 
it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """

    ### Please start your code here ###


    ### End ###


"""

Below are the test cases I created for testing the correctness of your code.
Please don't modify them when you push the file back to GitHub
"""

if __name__ == '__main__':
        test0 = (19, True)
        test1 = (22, False)
        test2 = (2018, False)
        tests = [test0, test1, test2]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0]
                print "-Expected Output:"
                print test[1]
                print "-Your Output:"
                your_ans = isHappy(test[0])
                print your_ans
                assert your_ans == test[1], "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'