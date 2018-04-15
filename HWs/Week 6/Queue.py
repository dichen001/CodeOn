# Queue class
class Queue(object):
    def __init__(self):
        # Start the queue
        self.queue = []
    def enQueue(self, val):
        # Append a new value to the queue
        self.queue.append(val)
    def deQueue(self):
        # Take out the first value in the list
        return self.queue.pop(0)
    def isEmpty(self):
        # Check if the queue is empty
        return self.queue == []
    def size(self):
        # Get the queue size
        return len(self.queue)