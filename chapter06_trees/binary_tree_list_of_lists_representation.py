# Properties of trees:
# 1. Trees are hierarchical, meaning trees are structured in layers with more general things near the top and the more
# specific things near the bottom.
# 2. All children of one node are independent of the children of another node.
# 3. Each leaf node is unique.
# 4. You can move entire sections of a tree (called a subtree) to a different position in the tree without affecting
# lower levels in the hierarchy.

# Examples of tree:
# - taxonomy
# - file systems
# - a web page

# Definitions:
# Node
# A node is a fundamental part of a tree. It can have a name, which we call the “key.” A node may also have
# additional information. We call this additional information the “payload.” While the payload information is not
# central to many tree algorithms, it is often critical in applications that make use of trees.
#
# Edge
# An edge is another fundamental part of a tree. An edge connects two nodes to show that there is a relationship
# between them. Every node (except the root) is connected by exactly one incoming edge from another node. Each node may
# have several outgoing edges.
#
# Root
# The root of the tree is the only node in the tree that has no incoming edges.
#
# Path
# A path is an ordered list of nodes that are connected by edges.
#
# Children
# The set of nodes that have incoming edges from the same node are said to be the children of that node.
#
# Parent
# A node is the parent of all the nodes it connects to with outgoing edges.
#
# Sibling
# Nodes in the tree that are children of the same parent are said to be siblings.
#
# Subtree
# A subtree is a set of nodes and edges comprised of a parent and all the descendants of that parent.
#
# Leaf Node
# A leaf node is a node that has no children.
#
# Level
# The level of a node is the number of edges on the path from the root node to n.
#
# Height
# The height of a tree is equal to the maximum level of any node in the tree.


def binary_tree(root):
    return [root, [], []]


def insert_left(tree, new_node):
    # Grab the existing left subtree.
    left_subtree = tree.pop(1)

    # Insert the new value in the tree. The new value is now the parent of the previous left subtree.
    if len(left_subtree) > 1:
        tree.insert(1, [new_node, left_subtree, []])
    else:
        tree.insert(1, [new_node, [], []])

    return tree


def insert_right(tree, new_node):
    # Grab the existing right subtree.
    right_subtree = tree.pop(2)

    # Insert the new value in the tree. The new value is now the parent of the previous right subtree.
    if len(right_subtree) > 1:
        tree.insert(2, [new_node, [], right_subtree])
    else:
        tree.insert(2, [new_node, [], []])

    return tree


def get_root_value(tree):
    """Get the root value of the given tree. The given tree may be a subtree."""

    return tree[0]


def set_root_value(tree, new_value):
    """Set the root value of the given tree. The given tree may be a subtree."""

    tree[0] = new_value


def get_left_child(tree):
    """Get the left child of the given tree. The given tree may be a subtree."""

    return tree[1]


def get_right_child(tree):
    """Get the right child of the given tree. The given tree may be a subtree."""

    return tree[2]


def main():
    print("Binary tree represented as a list of lists.")

    example_tree = binary_tree(3)
    print("Tree:", example_tree)

    insert_left(example_tree, 4)
    insert_left(example_tree, 5)
    insert_right(example_tree, 6)
    insert_right(example_tree, 7)
    left_child_subtree = get_left_child(example_tree)
    print("Left child subtree:", left_child_subtree)

    print("Tree:", example_tree)
    set_root_value(left_child_subtree, 9)
    print("Tree:", example_tree)

    insert_left(left_child_subtree, 11)
    print("Tree:", example_tree)

    print(get_right_child(get_right_child(example_tree)))


if __name__ == "__main__":
    main()
