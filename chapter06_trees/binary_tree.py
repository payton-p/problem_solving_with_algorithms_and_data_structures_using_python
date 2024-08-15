class BinaryTree:
    """A binary tree has a maximum of two children for each node."""

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """Insert into the left subtree of the given tree."""

        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            subtree = BinaryTree(new_node)
            subtree.left_child = self.left_child
            self.left_child = subtree

    def insert_right(self, new_node):
        """Insert into the right subtree of the given tree."""

        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            subtree = BinaryTree(new_node)
            subtree.right_child = self.right_child
            self.right_child = subtree

    def get_root_value(self):
        """Get the root value of the given tree. The given tree may be a subtree."""

        return self.key

    def set_root_value(self, obj):
        """Set the root value of the given tree. The given tree may be a subtree."""

        self.key = obj

    def get_left_child(self):
        """Get the left child of the given tree. The given tree may be a subtree."""

        return self.left_child

    def get_right_child(self):
        """Get the right child of the given tree. The given tree may be a subtree."""

        return self.right_child
