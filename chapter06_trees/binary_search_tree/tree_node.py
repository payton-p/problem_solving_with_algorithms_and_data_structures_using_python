class TreeNode:
    """
    The TreeNode class provides helper functions for many of the BinarySearchTree class methods

    One big difference between the TreeNode class and the BinaryTree class is that we will explicitly keep track of the
    parent as an attribute of each node.
    """

    def __init__(self, key, val, left=None, right=None, parent=None, *balance_factor):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

    def has_left_child(self):
        """Determine whether the current node has a left child."""

        return self.left_child

    def has_right_child(self):
        """Determine whether the current node has a right child."""

        return self.right_child

    def is_left_child(self):
        """Determine whether the current node is a left child."""

        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        """Determine whether the current node is a right child."""

        return self.parent and self.parent.right_child == self

    def is_root(self):
        """Determine whether the current node is the root node."""

        return not self.parent

    def is_leaf(self):
        """Determine whether the current node is a leaf node."""

        return not (self.right_child or self.left_child)

    def has_any_children(self):
        """Determine whether the current node has any children."""

        return self.right_child or self.left_child

    def has_both_children(self):
        """Determine whether the current node has both children."""

        return self.right_child and self.left_child

    def find_successor(self):
        """Find the successor. This is used in key deletion in the binary search tree."""

        successor = None

        # If the node has a right child, then the successor is the smallest key in the right subtree.
        if self.has_right_child():
            successor = self.right_child.find_minimum_child()
        else:
            if self.parent:
                # If the node has no right child and is the left child of its parent, then the parent is the successor.
                if self.is_left_child():
                    successor = self.parent
                # If the node is the right child of its parent, and itself has no right child, then the successor to
                # this node is the successor of its parent, excluding this node.
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self

        return successor

    def splice_out(self):
        """Remove the successor. This is used in key deletion in the binary search tree."""

        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_minimum_child(self):
        """Find the child with the smallest key for a given node."""

        current = self
        while current.has_left_child():
            current = current.left_child

        return current

    def replace_node_data(self, key, value, _left_child, _right_child):
        """Replace the data of a given node."""

        self.key = key
        self.payload = value
        self.left_child = _left_child
        self.right_child = _right_child

        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def __iter__(self):
        """Iterate over all the keys in the tree in order."""

        if self:
            if self.has_left_child():
                # This function is recursive because __iter__ overrides the "for x in . . . " operation.
                for key in self.left_child:
                    # "yield" is similar to return in that it returns a value to the caller. However, yield also takes
                    # the additional step of freezing the state of the function so that the next time the function is
                    # called it continues executing from the exact point it left off earlier. Functions that create
                    # objects that can be iterated are called generator functions.
                    yield key

            yield self.key

            if self.has_right_child():
                # This function is recursive because __iter__ overrides the "for x in . . . " operation.
                for key in self.right_child:
                    yield key
