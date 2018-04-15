"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    ### Please start your code here###

    # Target value
    for tval in t:
        if (not tval in s):
            return False
    return True


    ### End ###

"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ("anagram", "nagaram", True)
        test1 = ("rat","tar", True)
        test2 = ("sdfd","d987", False)
        test3 = ("23ss","ii", False)
        test4 = ("rat","rt", False)
        tests = [test0, test1, test2, test3, test4]
        for i, test in enumerate(tests):
                print("------------- Test " +str(i) + " -------------")
                print("-Test Input:")
                print(test[0], test[1])
                print("-Expected Output:")
                print(test[2])
                print("-Your Output:")
                your_ans = isAnagram(test[0], test[1])
                print(your_ans)
                print(test[2])
                assert your_ans == test[2], "Wrong return. Please try again."
        print('\n**** Congratulations! You have passed all the tests! ****')

