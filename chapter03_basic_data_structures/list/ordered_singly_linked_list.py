from chapter03_basic_data_structures.list.node import Node
from chapter03_basic_data_structures.list.singly_linked_list import SinglyLinkedList


class OrderedSinglyLinkedList(SinglyLinkedList):
    """
    A linked list is a linear collection of data elements whose order is not determined by the placement in memory.
    Instead, each element is stored in a node which points to the next node. In an ordered linked list, the relative
    positions of the items are based on some underlying characteristic.
    """

    def __init__(self):
        super().__init__()

        self.head = None

    def add(self, item):
        """Add a new node to the ordered singly linked list."""

        current = self.head
        previous = None

        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, item):
        """Search to see whether an item exists within the ordered linked list."""

        current = self.head

        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found
