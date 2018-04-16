"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

"""


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    ### Please start your code here###
    ans = []
    addedNums = {}
    for c_val in nums1:
        for c_val2 in nums2:
            if (c_val == c_val2):
                if (not c_val in addedNums):
                    addedNums[c_val] = 1
                    ans.append(c_val)
    return ans


    ### End ###

"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([1, 2, 2, 1], [2,2], [2])
        test1 = ([4,5,6,9],[7,22], [])
        test2 = ([44,55,22],[22], [22])
        test3 = ([3,5,7,9],[5,7,9], [5,7,9])
        tests = [test0, test1, test2, test3]
        for i, test in enumerate(tests):
                print("------------- Test " +str(i) + " -------------")
                print("-Test Input:")
                print(test[0], test[1])
                print("-Expected Output:")
                print(test[2])
                print("-Your Output:")
                your_ans = intersection(test[0], test[1])
                print(your_ans)
                assert (your_ans == test[2] or your_ans[::-1] == test[2]), "Wrong return. Please try again."
        print('\n**** Congratulations! You have passed all the tests! ****')


