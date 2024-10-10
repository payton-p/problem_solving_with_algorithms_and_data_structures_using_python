from chapter06_trees.binary_search_tree.binary_search_tree import BinarySearchTree
from chapter06_trees.binary_search_tree.tree_node import TreeNode


class AvlBinarySearchTree(BinarySearchTree):
    """
    An AVL binary search tree is a special kind of binary search tree that automatically makes sure the tree remains
    balanced at all times.

    This is a subclass of BinarySearchTree.
    """

    def __init__(self):
        self.root = None
        self.size = 0

        super().__init__()

    def _put(self, key, value, current_node):
        """
        This is a helper function that searches the tree and adds a new key-value pair to the map. It also keeps the
        tree in balance.

        Overrides the _put method in BinarySearchTree.
        """

        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        """
        Check to see if the current node is out of balance enough to require rebalancing. If that is the case, then the
        rebalancing is done and no further updating to parents is required. If the current node does not require
        rebalancing, then the balance factor of the parent is adjusted. If the balance factor of the parent is non-zero,
        then the algorithm continues to work its way up the tree toward the root by recursively calling update_balance
        on the parent.
        """

        # We will define a tree to be in balance if the balance factor is -1, 0, or 1. This should perform at O(log(n)).
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)

            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, old_root):
        """Left rotation. Rotations are performed on the tree to keep the tree balanced."""

        # Promote the right child to be the root of the tree.
        new_root = old_root.right_child
        old_root.right_child = new_root.left_child

        # If the new root already had a left child, then make it the right child of the new left child.
        if new_root.left_child is not None:
            new_root.left_child.parent = old_root

        new_root.parent = old_root.parent

        # Update parent of rotated root.
        if old_root.is_root():
            self.root = new_root
        else:
            if old_root.is_left_child():
                old_root.parent.left_child = new_root
            else:
                old_root.parent.right_child = new_root

        # Move the old root to be the left child of the new root.
        new_root.left_child = old_root
        old_root.parent = new_root

        # Update balance factor for old and new root. Since all other moves are moving entire subtrees around, the
        # balance factors of all other nodes are unaffected bby the rotation.
        old_root.balance_factor = old_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(old_root.balance_factor, 0)

    def rotate_right(self, old_root):
        """Right rotation. Rotations are performed on the tree to keep the tree balanced."""

        # Promote the left child to be the root of the tree.
        new_root = old_root.left_child
        old_root.left_child = new_root.right_child

        # If the new root already had a right child, then make it the left child of the new right child.
        if new_root.right_child is not None:
            new_root.right_child.parent = old_root

        new_root.parent = old_root.parent

        # Update parent of rotated root.
        if old_root.is_root():
            self.root = new_root
        else:
            if old_root.is_right_child():
                old_root.parent.right_child = new_root
            else:
                old_root.parent.left_child = new_root

        # Move the old root to be the right child of the new root.
        new_root.right_child = old_root
        old_root.parent = new_root

        # Update balance factor for old and new root.
        old_root.balance_factor = old_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(old_root.balance_factor, 0)

    def rebalance(self, node):
        """Perform rotations to keep the tree balanced."""

        # If a subtree needs a left rotation to bring it into balance, first check the balance factor of the right
        # child. If the right child is left heavy, then do a right rotation aon a right child, followed by the
        # original left rotation.
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        # If the subtree needs a right rotation to bring it into balance, first check the balance factor of the left
        # child. If the left child is right heavy, then do a left rotation on the left child, followed by the original
        # right rotation.
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)
