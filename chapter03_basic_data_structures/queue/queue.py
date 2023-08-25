class Queue:
    """A queue is an ordered collection of items. It follows FIFO (first in, first out)."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""

        return self.items == []

    def enqueue(self, item):
        """Add a new item to the rear of the queue."""

        self.items.insert(0, item)

    def dequeue(self):
        """Remove the front item from the queue."""

        return self.items.pop()

    def size(self):
        """Get the number of items in the queue."""

        return len(self.items)
