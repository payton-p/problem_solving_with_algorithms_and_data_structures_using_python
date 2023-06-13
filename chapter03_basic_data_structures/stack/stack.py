class Stack:
    """A stack is an ordered collection of items. It follows LIFO (last in, first out)."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""

        return self.items == []

    def peek(self):
        """See what item was last added to the stack."""

        return self.items[len(self.items) - 1]

    def pop(self):
        """Remove an item from the stack."""

        return self.items.pop()

    def push(self, item):
        """Add an item to the stack."""

        self.items.append(item)

    def size(self):
        """Get the number of items in the stack."""

        return len(self.items)

    def __str__(self):
        print(*self.items)
