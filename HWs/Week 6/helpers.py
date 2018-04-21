"""
DO NOT CHANGE THIS FILE!
This file contains all the helper functions related to a linked list.
"""
# Definition for singly-linked list.
class Node(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


# Given a head of a linked list. Return the list representation of this linked list.
def getLinkedList(head):
    node = head
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
    return nums

# Given a list of numbers, convert the given list into a linked list.
def createLinkedList(nums):
    pre = Node()
    node = pre
    for n in nums:
        node.next = Node(n)
        node = node.next
    return pre.next