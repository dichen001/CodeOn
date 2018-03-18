"""
Given an array of integers, every element appears twice except for one. Find that single one.

Example:

Given nums =[1,1,2,2,3], your function should return 3.


"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int

    Hint: use dictionary
    """




"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([1,1,2], 2)
        test1 = ([12,12,11,11,9,9,2], 2)
        tests = [test0, test1]
        for i, test in enumerate(tests):
                print("------------- Test " +str(i) + " -------------")
                print("-Test Input:")
                print(test[0])
                print("-Expected Output:")
                print(test[1])
                print("-Your Output:")
                your_ans = single_number(test[0])
                print(your_ans)
                assert your_ans == test[1], "Wrong return. Please try again."
        print('\n**** Congratulations! You have passed all the tests! ****')
