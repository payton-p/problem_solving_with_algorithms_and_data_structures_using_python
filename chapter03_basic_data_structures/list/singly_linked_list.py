class SinglyLinkedList:
    """
    A linked list is a linear collection of data elements whose order is not determined by the placement in memory.
    Instead, each element is stored in a node which points to the next node.
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        """Print the linked list."""

        readable_list = []

        node = self.head
        while node is not None:
            readable_list.append(node.data)
            node = node.next

        print(readable_list)

    def index(self, item):
        """Get the index of an item in the list."""

        count = 0
        node = self.head
        while node.get_data() != item:
            node = node.next
            count += 1

            if node is None:
                print("Item is not in list.")

                return -1

        return count

    def is_empty(self):
        """Check if the linked list is empty."""

        return self.head is None

    def pop(self):
        """Remove the last item in the linked list."""

        current = self.head
        if self.head is None:
            print("The list is empty.")

        # Get the last node.
        while current.get_next() is not None:
            current = current.get_next()

        # Remove the last node.
        if current.get_next() is None:
            self.remove(current.get_data())

    def pop_by_position(self, position):
        """Remove a node in the linked list at the position given."""

        previous = self.head
        current = previous.next

        if self.index(previous.get_data()) == position:
            self.remove(previous.get_data())
        else:
            while self.index(current.get_data()) != position:
                previous = previous.next
                current = current.next
                if current is None:
                    print("Item is not in list.")

            self.remove(current.get_data())
            previous.set_next(current.next)

    def remove(self, item):
        """Remove a node from the linked list by the value given."""

        current = self.head
        previous = None

        # Find the item in the linked list.
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        # Modify the linked list so the node is removed.
        if previous is None:  # handles special case where item to be removed happens to be the first item in the list
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def size(self):
        """Get the number of nodes in the linked list."""

        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count
