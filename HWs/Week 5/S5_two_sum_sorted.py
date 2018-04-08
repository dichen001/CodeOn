"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 

Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and 

you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

def twoSumSorted(numbers, target):
    """
    :param numbers: list
    :param target: int
    :return: list 
    """


    ### Please start your code here###

    storage = {}
    for indx, cval in enumerate(numbers):
        tval = target - cval
        if (tval in storage):
            return [storage[tval]+1, indx+1]
        storage[cval] = indx

    ### End ###





"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([2,7,11,15], 9, [1, 2])
        test1 = ([1,5,9],10, [1,3])
        test2 = ([2,3,4], 6, [1,3])
        tests = [test0, test1, test2]
        for i, test in enumerate(tests):
                print("------------- Test " +str(i) + " -------------")
                print("-Test Input:")
                print(test[0], test[1])
                print("-Expected Output:")
                print(test[2])
                print("-Your Output:")
                your_ans = twoSumSorted(test[0], test[1])
                print(your_ans)
                assert (your_ans == test[2] or your_ans[::-1] == test[2]), "Wrong return. Please try again."
        print('\n**** Congratulations! You have passed all the tests! ****')

