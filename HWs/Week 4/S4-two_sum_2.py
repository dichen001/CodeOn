"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    ans = []
    d = {}
    for indx, c_val in enumerate(nums):
        tVal = target - c_val
        if (not d.get(tVal, False)):
            d[tVal] = indx
        else:
            ans.append(indx, d[tVal])
    return ans


"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([2,7,11,15], 9, [0, 1])
        test1 = ([1,5,9],10, [0,2])
        test2 = ([2,3,4], 6, [0,2])
        tests = [test0, test1, test2]
        for i, test in enumerate(tests):
                print("------------- Test " +str(i) + " -------------")
                print("-Test Input:")
                print(test[0], test[1])
                print("-Expected Output:")
                print(test[2])
                print("-Your Output:")
                your_ans = two_sum(test[0], test[1])
                print(your_ans)
                assert (your_ans == test[2] or your_ans[::-1] == test[2]), "Wrong return. Please try again."
        print('\n**** Congratulations! You have passed all the tests! ****')

