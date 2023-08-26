from chapter03_basic_data_structures.list.node import Node
from chapter03_basic_data_structures.list.singly_linked_list import SinglyLinkedList


class UnorderedSinglyLinkedList(SinglyLinkedList):
    """
    A linked list is a linear collection of data elements whose order is not determined by the placement in memory.
    Instead, each element is stored in a node which points to the next node. For unordered linked lists, as long as we
    know where to find the first node (containing the first item), each item after that can be found by successively
    following the next links.
    """

    def __init__(self):
        super().__init__()

        self.head = None

    def add(self, item):
        """
        Add a new node to the unordered linked list. We add the new node in the simplest way, which means we add it as
        the new head.
        """

        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

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
