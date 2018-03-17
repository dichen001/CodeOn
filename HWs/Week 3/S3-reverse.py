"""
Reverse a singly linked list.

Input: 1->2->3
Output: 3->2->1

Input: 1
Output: 1
"""

from helpers import Node, getLinkedList, createLinkedList
import random
def reverseList(head):
        """
        :type head: Node
        :rtype: Node
        """
        ### Please write your code inside ###


        # I was having trouble with the problem, so I searched up some answeres online

        # I found this one that seems to work but I still cant understand the explanations
        new_head = None  # this is where we build the reversed list (reusing the existing nodes)
        while head:
            temp = head  # temp is a reference to a node we're moving from one  list to the other
            head = temp.next  # the first two assignments pop the node off the front of the list
            temp.next = new_head  # the next two make it the new head of the reversed list
            new_head = temp

        return new_head
        ### Please write your code inside ###


"""
Below are the test cases I created for testing the correctness of your code.

Please don't modify them when you push the file back to GitHub
"""
if __name__ == '__main__':
        test0 = ([], [])
        test1 = ([1], [1])
        test2 = ([1,2], [2,1])
        test3 = ([1,2,3], [3,2,1])
        test4 = ([1,1,2,3,3], [3,3,2,1,1])
        random_list0 = [random.randint(1,10) for _ in range(20)]
        test5 = (random_list0, random_list0[::-1])
        random_list1 = [random.randint(1,10) for _ in range(100)]
        test6 = (random_list1, random_list1[::-1])
        tests = [test0, test1, test2, test3, test4, test5, test6]
        for i, test in enumerate(tests):
                print "------------- Test " +str(i) + " -------------"
                print "-Test Input:"
                print test[0]
                print "-Expected Output:"
                print test[1]
                print "-Your Output:"
                head = createLinkedList(test[0])
                your_head = reverseList(head)
                your_ans = getLinkedList(your_head)
                print your_ans
                assert your_ans == test[1], "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'
