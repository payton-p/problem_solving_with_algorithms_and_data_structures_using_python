class Node:
    """A node contains a data field and a reference (link) to the next node in the linked list."""

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        """Get the data field."""

        return self.data

    def set_data(self, new_data):
        """Set the data field."""

        self.data = new_data

    def get_next(self):
        """Get the reference (link) the next node in the linked list."""

        return self.next

    def set_next(self, new_next):
        """Set the reference (link) the next node in the linked list."""

        self.next = new_next
