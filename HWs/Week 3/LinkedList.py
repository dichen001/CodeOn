class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def ins(self, node=None):
        if node:
            node.next = self.head
            self.head = node

    def getLen(self):
        node = self.head
        cLen = 0
        while node:
            cLen += 1
            node = node.next
        return cLen

    def printll(self):
        node=self.head
        while node:
            print node.val
            node = node.next

    def remove(self, val=None):
        # Start at 3
        cur = self.head
        # None
        pre = None

        if self.head and val == self.head.val:
            self.head = cur.next
            return

        # There is a head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

ll = LinkedList()
ll.remove(1)
ll.head = Node(1)
ll.ins(Node(2))
ll.ins(Node(3))

#ll.remove(3)
ll.printll()