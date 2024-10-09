from chapter06_trees.binary_search_tree.binary_search_tree import BinarySearchTree


def main():
    tree = BinarySearchTree()

    # Test the put method.
    tree[3] = "red"  # uses the __setitem__ magic method.
    tree[4] = "blue"
    tree[6] = "yellow"
    tree[2] = "at"

    # Test the get method.
    print(tree[6])  # uses the __getitem__ magic method.
    print(tree[2])

    # Test length method.
    print("Size of tree:", len(tree))  # uses the __len__ magic method.

    # Test the in operation.
    if 6 in tree:  # uses the __contains__ magic method.
        print("Found in tree.")
    else:
        print("Not found in tree.")

    if 18 in tree:
        print("18 found in tree.")
    else:
        print("18 not found in tree.")

    # Test deletion.
    if 2 in tree:
        print("2 found in tree.")
    else:
        print("2 not found in tree.")

    del tree[2]  # uses the __delitem__ magic method.

    if 2 in tree:
        print("2 found in tree.")
    else:
        print("2 not found in tree.")

    # Test iteration.
    print("Keys in tree:")
    for key in tree:  # uses the __iter__ magic method.
        print(key)


if __name__ == "__main__":
    main()
