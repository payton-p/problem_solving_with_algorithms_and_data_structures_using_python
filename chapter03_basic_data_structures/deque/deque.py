class Deque:
    """
    A deque, also known as a double-ended queue, is an ordered collection of items. It has two ends, a front and a rear,
    and the items remain positioned in the collection. New items can be added or removed at either the front or the
    rear.

    This implementation assumes that the rear of the deque is at position 0 in the list.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the deque is empty."""

        return self.items == []

    def add_front(self, item):
        """Add a new item to the front of the deque."""

        self.items.append(item)

    def add_rear(self, item):
        """Add a new item to the rear of the deque."""

        self.items.insert(0, item)

    def remove_front(self):
        """Remove the front item from the deque."""

        return self.items.pop()

    def remove_rear(self):
        """Remove the rear item from the deque."""

        return self.items.pop(0)

    def size(self):
        """Get the number of items in the deque."""

        return len(self.items)
