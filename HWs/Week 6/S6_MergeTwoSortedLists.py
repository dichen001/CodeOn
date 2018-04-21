"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


from helpers import Node, getLinkedList, createLinkedList

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeTwoLists(l1, l2):
		"""
	  l1: ListNode
	  l2: ListNode
	  """

    ### Please start your code here###



    # ### End ###


"""

Below are the test cases I created for testing the correctness of your code.
Please don't modify them when you push the file back to GitHub
"""

if __name__ == '__main__':
        test0 = ([], [], [])
        test1 = ([1], [1], [1, 1])
        test2 = ([1,2], [3,4,5,6], [1,2,3,4,5,6])
        test3 = ([1,2,3], [1,2,3], [1,1,2,2,3,3,])
        tests = [test0, test1, test2, test3]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0]
                print "-Expected Output:"
                print test[1]
                print "-Your Output:"
                head1 = createLinkedList(test[0])
                head2 = createLinkedList(test[1])
                your_head = mergeTwoLists(head1, head2)
                your_ans = getLinkedList(your_head)
                print your_ans
                assert your_ans == test[2], "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'
        