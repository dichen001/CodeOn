"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

from helpers import Node, getLinkedList, createLinkedList

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    """
    :type head: Node
    :rtype: Node
    """
    ### Please write your code inside ###




    ### Please write your code inside ###





"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([], [])
        test1 = ([1], [1])
        test2 = ([1,1], [1])
        test3 = ([1,1,2], [1, 2])
        test4 = ([1,1,2,3,3], [1,2,3])
        tests = [test0, test1, test2, test3, test4]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0]
                print "-Expected Output:"
                print test[1]
                print "-Your Output:"
                head = createLinkedList(test[0])
                your_head = deleteDuplicates(head)
                your_ans = getLinkedList(your_head)
                print your_ans
                assert your_ans == test[1], "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'
