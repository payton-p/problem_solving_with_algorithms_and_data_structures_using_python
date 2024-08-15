from chapter06_trees.min_heap_binary_tree import MinHeapBinaryTree


def main():
    min_heap_binary_tree = MinHeapBinaryTree()
    min_heap_binary_tree.build_min_heap([9, 5, 6, 2, 3])

    print("Min value deleted:", min_heap_binary_tree.delete_min())
    print("Min value deleted:", min_heap_binary_tree.delete_min())
    print("Min value deleted:", min_heap_binary_tree.delete_min())
    print("Min value deleted:", min_heap_binary_tree.delete_min())
    print("Min value deleted:", min_heap_binary_tree.delete_min())

    print("Insert values.")
    min_heap_binary_tree.insert(55)
    min_heap_binary_tree.insert(1)
    min_heap_binary_tree.insert(13)
    print("Min value deleted:", min_heap_binary_tree.delete_min())


if __name__ == "__main__":
    main()
