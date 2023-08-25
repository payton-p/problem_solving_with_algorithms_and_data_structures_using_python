from chapter03_basic_data_structures.list.node import Node


class UnorderedLinkedList:
    """
    A linked list is a linear collection of data elements whose order is not determined by the placement in memory.
    Instead, each element is stored in a node which points to the next node. For unordered linked lists, as long as we
    know where to find the first node (containing the first item), each item after that can be found by successively
    following the next links.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the unordered linked list is empty."""

        return self.head is None

    def add(self, item):
        """
        Add a new node to the unordered linked list. We add the new node in the simplest way, which means we add it as
        the new head.
        """

        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Get the number of nodes in the unordered linked list."""

        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        """Search to see whether an item exists within the unordered linked list."""

        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        """Remove a node from the unordered linked list by the value given."""

        current = self.head
        previous = None

        # Find the item in the unordered linked list.
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        # Modify the unordered linked list so the node is removed.
        if previous is None:  # handles special case where item to be removed happens to be the first item in the list
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print_list(self):
        """Print the unordered linked list."""

        readable_list = []

        node = self.head
        while node is not None:
            readable_list.append(node.data)
            node = node.next

        print(readable_list)

    def append(self, item):
        """Add a new node to the end of the unordered linked list."""

        new_node = Node(item)
        node = self.head

        # If the list is empty, set the new node as the head.
        if self.head is None:
            self.head = new_node

        # Find the item at the end of the list.
        while node.get_next() is not None:
            node = node.get_next()

        # Add the new node to the end of the list.
        node.set_next(new_node)

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

    def insert(self, position, item):
        """Insert a node at a specific position in the linked list."""

        new_node = Node(item)
        previous = self.head
        current = previous.next

        if position == 0:  # adds as the new head
            self.add(item)
        elif position == self.size() - 1:  # appends to end
            self.append(item)
        elif position > self.size() - 1:  # handles an invalid position
            print("Invalid position.")
        else:
            # Find the correct position.
            while self.index(current.get_data()) != position:
                previous = previous.next
                current = current.next

            # Add the new node to that position.
            previous.set_next(new_node)
            new_node.set_next(current)

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
            current = self.head

        while self.index(current.get_data()) != position:
            previous = previous.next
            current = current.next
            if current is None:
                print("Item is not in list.")

        if self.index(current.get_data()) == position:
            self.remove(current.get_data())
            previous.set_next(current.next)
