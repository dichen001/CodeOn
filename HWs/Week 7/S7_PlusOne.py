"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,

and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.


Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""



def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    ### Please start your code here ###

    for c in reversed(range(len(digits))):
        print "....", c
        if digits[c] == 9:
            digits[c] = 0
        else:
            digits[c] += 1
            return digits

    # A bit confused about this part
    digits[0] = 1
    digits.append(0)
    return digits

    ### End ###


"""

Below are the test cases I created for testing the correctness of your code.
Please don't modify them when you push the file back to GitHub
"""

if __name__ == '__main__':
        test0 = ([1,2,3], [1,2,4])
        test1 = ([9,9,9], [1,0,0,0])
        test2 = ([0], [1])
        tests = [test0, test1, test2]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0]
                print "-Expected Output:"
                print test[1]
                print "-Your Output:"
                your_ans = plusOne(test[0])
                print your_ans
                assert your_ans == test[1], "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'