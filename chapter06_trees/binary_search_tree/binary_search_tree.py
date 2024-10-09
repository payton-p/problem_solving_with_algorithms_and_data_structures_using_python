from chapter06_trees.binary_search_tree.tree_node import TreeNode


class BinarySearchTree:
    """
    A binary search tree relies on the property that keys that are less than the parent are found in the left subtree,
    and keys that are greater than the parent are found in the right subtree.
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        """
        Return the number of key-value pairs stored in the map.

        Dunder (or magic) methods are double underscored methods that are used to emulate the behavior of built-in
        types. They are predefined methods that simplify many operations that can be performed on a class instance. But,
        these methods are used only in indexed attributes like arrays, dictionaries, lists, etc. Instead of directly
        accessing and manipulating class attributes, it provides such methods, so these attributes can be modified only
        by its own instances and thus implements abstraction.

        Example of where this is used:
        tree = BinarySearchTree()
        tree[2] = "green"
        len(tree)  # it is used during this operation
        """

        return self.size

    def put(self, key, val):
        """
        Add a new key-value pair to the map.

        If the key is already in the map then replace the old value with the new value.
        """

        # Check if the tree already has a root. If it does, add the new key-value pair to the appropriate place in the
        # tree.
        if self.root:
            self._put(key, val, self.root)
        # If it does not have a root, then create a new tree node and set it as the root of the tree.
        else:
            self.root = TreeNode(key, val)

        self.size = self.size + 1

    def _put(self, key, val, current_node):
        """This is a helper function that searches the tree and adds a new key-value pair to the map."""

        # TODO: duplicate keys are not handled correctly.

        # If the new key is less than the current node, search the left subtree.
        if key < current_node.key:
            # Continue searching.
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            # When there is no left child to search, we have found the position in the tree where the new node should
            # be added. When a new child is inserted into the tree, the current node is passed to the new tree node as
            # the parent.
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        # If the new key is greater than the current node, search the right subtree.
        else:
            # Continue searching.
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            # When there is no right child to search, we have found the position in the tree where the new node should
            # be added. When a new child is inserted into the tree, the current node is passed to the new tree node as
            # the parent.
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):
        """
        Set value of item.

        Dunder (or magic) methods are double underscored methods that are used to emulate the behavior of built-in
        types. They are predefined methods that simplify many operations that can be performed on a class instance. But,
        these methods are used only in indexed attributes like arrays, dictionaries, lists, etc. Instead of directly
        accessing and manipulating class attributes, it provides such methods, so these attributes can be modified only
        by its own instances and thus implements abstraction.

        Example of where this is used:
        tree = BinarySearchTree()
        tree[3] = "red"  # it is used during this operation
        """

        self.put(key, value)

    def get(self, key):
        """Given a key, return the value stored in the map, otherwise return None."""

        if self.root:
            result = self._get(key, self.root)

            if result:
                return result.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        """
        This is a helper function that searches the tree until it gets to a non-matching leaf or finds a matching key.

        When a matching key is found, the value is stored in the payload of the node and is returned.
        """

        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        """
        Get value of item.

        Dunder (or magic) methods are double underscored methods that are used to emulate the behavior of built-in
        types. They are predefined methods that simplify many operations that can be performed on a class instance. But,
        these methods are used only in indexed attributes like arrays, dictionaries, lists, etc. Instead of directly
        accessing and manipulating class attributes, it provides such methods, so these attributes can be modified only
        by its own instances and thus implements abstraction.

        Example of where this is used:
        tree = BinarySearchTree()
        tree[3] = "red"
        print(tree[3])  # it is used during this operation
        """

        return self.get(key)

    def __contains__(self, key):
        """
        Determine whether collection contains an item.

        Dunder (or magic) methods are double underscored methods that are used to emulate the behavior of built-in
        types. They are predefined methods that simplify many operations that can be performed on a class instance. But,
        these methods are used only in indexed attributes like arrays, dictionaries, lists, etc. Instead of directly
        accessing and manipulating class attributes, it provides such methods, so these attributes can be modified only
        by its own instances and thus implements abstraction.

        Example of where this is used:
        tree = BinarySearchTree()
        tree[3] = "red"
        print(tree[3])  # it is used during this operation
        """

        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """Delete the key-value pair from the map."""

        if self.size > 1:
            # Find the node to delete.
            node_to_remove = self._get(key, self.root)

            # Remove the specified node.
            if node_to_remove:
                self._delete(node_to_remove)
                self.size = self.size - 1
            # If the key is not found, raise an error.
            else:
                raise KeyError("Error: key not in tree.")
        # If there is only one node and the key matches, remove the root of the tree.
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        # If the key is not found, raise an error.
        else:
            raise KeyError("Error: key not in tree.")

    @staticmethod
    def _delete(current_node):
        """This is a helper function that deletes a specified node from the map."""

        # The node is a leaf, meaning it is a node that has on children. To do this, the node is deleted and the
        # reference to this node is removed from the parent.
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        # The node has two children, so it is an interior node.
        elif current_node.has_both_children():
            # Search the tree for a node that can be used to replace the one scheduled for deletion. The node that will
            # accomplish this is the node that has the next largest key in the tree. We call this node the successor.
            # The successor is guaranteed to have no more than one child.
            successor = current_node.find_successor()

            # Remove the successor.
            successor.splice_out()

            # Once the successor has been removed, we put it in the tree in place of the node to be deleted.
            current_node.key = successor.key
            current_node.payload = successor.payload
        # The node has one child. To do this, we promote the single child node to take the place of its parent.
        else:
            # The current node's one child is a left child.
            if current_node.has_left_child():
                # Update parent reference of the left child to point to the parent of the current node, then update the
                # left child reference of the parent to point to the current node's left child.
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                # Update the parent reference of the right child to point to the parent of the current node, and then
                # update the right child reference of the parent to point to the current node's right child.
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                # Current node has no parent, so it must be the root. Replace the key, payload, left child, and right
                # child data by calling replace_node_data on the root.
                else:
                    current_node.replace_node_data(current_node.left_child.key, current_node.left_child.payload,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            # The current node's one child is a right child. Symmetric logic follows as described for the case of having
            # one left child (seen above).
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key, current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)

    def __delitem__(self, key):
        """
        Delete an item.

        Dunder (or magic) methods are double underscored methods that are used to emulate the behavior of built-in
        types. They are predefined methods that simplify many operations that can be performed on a class instance. But,
        these methods are used only in indexed attributes like arrays, dictionaries, lists, etc. Instead of directly
        accessing and manipulating class attributes, it provides such methods, so these attributes can be modified only
        by its own instances and thus implements abstraction.

        Example of where this is used:
        tree = BinarySearchTree()
        tree[2] = "green"
        del tree[2]  # it is used during this operation
        """

        self.delete(key)

    def __iter__(self):
        """
        Make collection iterable.

        Dunder (or magic) methods are double underscored methods that are used to emulate the behavior of built-in
        types. They are predefined methods that simplify many operations that can be performed on a class instance. But,
        these methods are used only in indexed attributes like arrays, dictionaries, lists, etc. Instead of directly
        accessing and manipulating class attributes, it provides such methods, so these attributes can be modified only
        by its own instances and thus implements abstraction.

        Example of where this is used:
        tree = BinarySearchTree()
        tree[2] = "green"
        for key in tree:  # it is used during this operation
            print(key)
        """

        return self.root.__iter__()
