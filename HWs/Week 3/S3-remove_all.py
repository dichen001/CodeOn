"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

"""

from helpers import Node, getLinkedList, createLinkedList

def removeElements(head, val):
    """
    :type head: Node
    :type val: int
    :rtype: Node
    """
    # Please write your code inside

    lArray = getLinkedList(head)
    lNewArray = []

    for lVal in lArray:
        if lVal != val:
            lNewArray.append(lVal)

    ll = createLinkedList(lNewArray)

    return ll

    # Please write your code inside



"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([1,1,1,1], 1, [])
        test1 = ([3,1,2,3], 1, [3,2,3])
        test2 = ([3,1,2,3], 2, [3,1,3])
        test3 = ([3,1,2,3], 3, [1,2])
        tests = [test0, test1, test2, test3]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0], test[1]
                print "-Expected Output:"
                print test[2]
                print "-Your Output:"
                head = createLinkedList(test[0])
                val = test[1]
                your_head = removeElements(head, val)
                your_ans = getLinkedList(your_head)
                print your_ans
                assert your_ans == test[2], "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'
