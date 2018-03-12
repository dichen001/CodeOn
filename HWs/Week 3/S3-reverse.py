"""
Reverse a singly linked list.

Input: 1->2->3
Output: 3->2->1

Input: 1
Output: 1
"""

from helpers import Node, getLinkedList, creatLinkedList
import random
def reverseList(head):
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
                head = creatLinkedList(test[0])
                your_head = reverseList(head)
                your_ans = getLinkedList(your_head)
                print your_ans
                assert your_ans == test[1], "Wrong return. Please try again."
        print '\n**** Congratulations! You have passed all the tests! ****'
