from chapter06_trees.binary_tree import BinaryTree


def main():
    print("Binary tree represented as a nodes and references.")

    example_tree = BinaryTree("a")
    print(example_tree.get_root_value())
    print(example_tree.get_left_child())

    example_tree.insert_left("b")
    print(example_tree.get_left_child().get_root_value())

    example_tree.insert_right("c")
    print(example_tree.get_right_child().get_root_value())

    example_tree.get_right_child().set_root_value("hello")
    print(example_tree.get_right_child().get_root_value())


if __name__ == "__main__":
    main()
