from chapter06_trees.binary_tree import BinaryTree


def preorder(tree):
    """
    In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left
    subtree, followed by a recursive preorder traversal of the right subtree.
    """

    if tree:
        print(tree.get_root_value())

        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def inorder(tree):
    """
    In an inorder traversal, we recursively do an inorder traversal on the left subtree, visit the root node, and
    finally do a recursive inorder traversal of the right subtree.
    """

    if tree is not None:
        inorder(tree.get_left_child())
        print(tree.get_root_value())

        inorder(tree.get_right_child())


def postorder(tree):
    """
    In a postorder traversal, we recursively do a postorder traversal of the left subtree and the right subtree
    followed by a visit to the root node.
    """

    if tree is not None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())

        print(tree.get_root_value())


def main():
    print("Tree traversals.")

    example_tree = BinaryTree("a")
    example_tree.insert_left("b")
    example_tree.insert_right("c")

    print("Preorder traversal:")
    preorder(example_tree)

    print("\nInorder traversal:")
    inorder(example_tree)

    print("\nPostorder traversal:")
    postorder(example_tree)


if __name__ == "__main__":
    main()
