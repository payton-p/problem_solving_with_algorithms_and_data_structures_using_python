from chapter06_trees.binary_search_tree.avl_binary_search_tree import AvlBinarySearchTree


def main():
    # What is the height of a binary tree likely to be? That depends on how the keys are added. If they keys are added
    # in random order, the height will be around log2(n). This is because, if the keys are randomly distributed, about
    # half will be less than the root.

    # The number of nodes at any particular level is 2^d, where d is the depth of the level. The number of nodes in a
    # perfectly balanced binary tree is 2^(h +1)-1, where h represents the height of the tree. A perfectly balanced tree
    # has the same number of nodes in the left subtree as the right. In a balanced binary tree, the worst case
    # performance of put() is O(log2(n)), where n is the number of nodes in the tree.

    # It is possible to construct a search tree that has height n simply by inserting the keys in sorted order. In this
    # case, performance of the put() method is O(n).

    # Making sure a tree stays balanced:
    # There is a special kind of binary search tree that automatically makes sure the tree remains balanced at all
    # times. This tree is called an AVL tree (it is named after its inventors). An AVL tree implements the Map abstract
    # data type just like a regular binary search tree, the only difference is in how the tree performs. To implement
    # our AVL tree we need to keep track of a "balance factor" for each node in the tree. We do this by looking at the
    # heights of the left and right subtrees for each node.
    # balance factor = height of left subtree - height of right subtree
    # We say that a subtree is left-heavy if the balance factor > 0.
    # We say that a subtree is right-heavy if the balance factor < 0.
    # If the balance factor is zero, the tree is perfectly balanced.

    # We will define a tree to be in balance if the balance factor is -1, 0, or 1. This should perform at O(log(n)).

    # Our put() operation remains O(log2(n)) with the AvlBinarySearchTree implementation.

    simple_tree = AvlBinarySearchTree()
    simple_tree[1] = "red"
    simple_tree[2] = "blue"
    simple_tree[3] = "yellow"

    print(simple_tree.get_root_key(), simple_tree.get_root_value())

    complex_tree = AvlBinarySearchTree()
    complex_tree["E"] = "red"
    complex_tree["C"] = "blue"
    complex_tree["F"] = "green"
    complex_tree["B"] = "pink"
    complex_tree["D"] = "purple"
    complex_tree["A"] = "orange"

    print(complex_tree.get_root_key(), complex_tree.get_root_value())

    another_tree = AvlBinarySearchTree()
    another_tree["A"] = "pink"
    another_tree["C"] = "purple"
    another_tree["B"] = "orange"

    print(another_tree.get_root_key(), another_tree.get_root_value())


if __name__ == "__main__":
    main()
