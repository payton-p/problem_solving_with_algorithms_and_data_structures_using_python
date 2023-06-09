from chapter03_basic_data_structures.stacks.stack import Stack


# The Divide by 2 algorithm assumes that we start with an integer greater than 0. A simple iteration then continually
# divides the decimal number by 2 and keeps track of the remainder.
def divide_by_two_algorithm(number):
    remainder_stack = Stack()

    while number > 0:
        remainder = number % 2
        remainder_stack.push(remainder)
        number = number // 2

    # The top of the stack is the start of the binary string.
    binary_string = ""
    while not remainder_stack.is_empty():
        binary_string = binary_string + str(remainder_stack.pop())

    return binary_string


def main():
    print(divide_by_two_algorithm(42))
    print(divide_by_two_algorithm(233))


if __name__ == "__main__":
    main()
