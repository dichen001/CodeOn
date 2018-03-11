def start(nums, val):

    nums_len = len(nums)
    val_ctr = 0
    ans_array = []

    for n_val in nums:
        if n_val != val:
            ans_array.append(n_val)
        else:
            val_ctr += 1

    for inx in range(val_ctr):
        ans_array.append(val)

    return len(nums)-val_ctr

start([2,2,3,2], 2)

"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
    test0 = ([], 1, 0)
    test1 = ([2, 3, 2], 2, 1)
    test2 = ([2, 3, 2], 3, 2)
    test3 = ([2, 3, 3, 1, 2, 2], 2, 3)
    test4 = ([2, 3, 3, 1, 2, 2], 1, 5)
    test5 = ([2, 3, 3, 1, 2, 2], 3, 4)
    tests = [test0, test1, test2, test3, test4, test5]
    for i, test in enumerate(tests):
        print "------------- Test " + str(i) + " -------------"
        print "-Test Input:"
        print test[0:2]
        print "-Expected Output:"
        print test[2]
        print "-Your Output:"
        print start(test[0], test[1])
        assert start(test[0], test[1]) == test[2], "Wrong return. Please try again."
    print '\n**** Congratulations! You have passed all the tests! ****'
