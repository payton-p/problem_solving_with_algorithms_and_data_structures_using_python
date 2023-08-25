from chapter03_basic_data_structures.list.unordered_linked_list import UnorderedLinkedList


def main():
    unordered_linked_list = UnorderedLinkedList()

    # Add 7 nodes.
    unordered_linked_list.add(7)
    unordered_linked_list.add(6)
    unordered_linked_list.add(5)
    unordered_linked_list.add(4)
    unordered_linked_list.add(3)
    unordered_linked_list.add(2)
    unordered_linked_list.add(1)

    # Print initial list.
    unordered_linked_list.print_list()

    print("List size:", unordered_linked_list.size())
    print("Search for 5:", unordered_linked_list.search(5))
    print("Search for 100:", unordered_linked_list.search(100))
    print("List is empty:", unordered_linked_list.is_empty())

    # Add new node.
    print("Add a new node (8).")
    unordered_linked_list.add(8)
    unordered_linked_list.print_list()

    # Remove node.
    print("Remove a node (4).")
    unordered_linked_list.remove(4)
    unordered_linked_list.print_list()

    # Append a new node.
    print("Append a new node (9).")
    unordered_linked_list.append(9)
    unordered_linked_list.print_list()

    # Get the index of a node.
    node_index = unordered_linked_list.index(3)
    print("Get index of a node (3).", node_index)
    node_index = unordered_linked_list.index(1000)
    print("Get index of a node (1000).", node_index)

    # Insert a new node.
    print("Insert new nodes.")
    unordered_linked_list.insert(3, 10)  # inserts into the middle
    unordered_linked_list.print_list()
    unordered_linked_list.insert(0, 11)  # inserts at the head
    unordered_linked_list.print_list()
    unordered_linked_list.insert(unordered_linked_list.size() - 1, 12)  # inserts at the end
    unordered_linked_list.print_list()

    # Pop the last node off the linked list.
    print("Pop the last item off the linked list.")
    unordered_linked_list.pop()
    unordered_linked_list.print_list()

    # Pop nodes off the linked list by the index given.
    print("Pop nodes off the linked list by the index given.")
    unordered_linked_list.pop_by_position(0)  # pops the preexisting head
    unordered_linked_list.print_list()
    unordered_linked_list.pop_by_position(2)  # pops a node from the middle
    unordered_linked_list.print_list()
    unordered_linked_list.pop_by_position(unordered_linked_list.size() - 1)  # pops the end node
    unordered_linked_list.print_list()


if __name__ == "__main__":
    main()
