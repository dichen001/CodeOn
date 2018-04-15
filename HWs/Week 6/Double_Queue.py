# Double Queue class
# Allows you to insert items at the front and back of list
class Double_Queue(object):
    def __init__(self):
        # Start list
        self.queue = []
    def addFront(self, val):
        # Insert in the front of the list
        self.queue.insert(0, val)
    def addBack(self, val):
        # Insert at the back of the list
        self.queue.append(val)
    def removeFront(self, val):
        # Remove value at the front of the list
        return self.queue.pop(0)
    def removeBack(self, val):
        # Remove value at the back of the list
        return self.queue.pop()
    def isEmpty(self):
        # Check if the list is empty
        return self.queue == []
    def size(self):
        # Get the size of the list
        return len(self.queue)

