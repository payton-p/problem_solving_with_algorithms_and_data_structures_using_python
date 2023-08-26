from chapter03_basic_data_structures.list.ordered_singly_linked_list import OrderedSinglyLinkedList


def main():
    ordered_linked_list = OrderedSinglyLinkedList()

    # Add 7 nodes.
    ordered_linked_list.add(7)
    ordered_linked_list.add(6)
    ordered_linked_list.add(5)
    ordered_linked_list.add(4)
    ordered_linked_list.add(3)
    ordered_linked_list.add(2)
    ordered_linked_list.add(1)

    # Print initial list.
    ordered_linked_list.__str__()

    print("List size:", ordered_linked_list.size())
    print("Search for 5:", ordered_linked_list.search(5))
    print("Search for 100:", ordered_linked_list.search(100))
    print("List is empty:", ordered_linked_list.is_empty())

    # Add new node.
    print("Add a new node (8).")
    ordered_linked_list.add(8)
    ordered_linked_list.__str__()

    # Remove node.
    print("Remove a node (4).")
    ordered_linked_list.remove(4)
    ordered_linked_list.__str__()

    # Get the index of a node.
    node_index = ordered_linked_list.index(3)
    print("Get index of a node (3):", node_index)
    node_index = ordered_linked_list.index(1000)
    print("Get index of a node (1000):", node_index)

    # Pop the last node off the linked list.
    print("Pop the last item off the linked list.")
    ordered_linked_list.pop()
    ordered_linked_list.__str__()

    # Pop nodes off the linked list by the index given.
    print("Pop nodes off the linked list by the index given.")
    ordered_linked_list.pop_by_position(0)  # pops the preexisting head
    ordered_linked_list.__str__()
    ordered_linked_list.pop_by_position(2)  # pops a node from the middle
    ordered_linked_list.__str__()
    ordered_linked_list.pop_by_position(ordered_linked_list.size() - 1)  # pops the end node
    ordered_linked_list.__str__()


if __name__ == "__main__":
    main()
