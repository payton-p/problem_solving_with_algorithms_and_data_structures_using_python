from chapter03_basic_data_structures.stack.stack import Stack


def balanced_parentheses_checker(symbol_string):
    stack = Stack()
    balanced = True

    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            stack.push(symbol)
            print("Push:", stack.__str__())
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
                print("Pop:", stack.__str__())

        index = index + 1

    return balanced and stack.is_empty()


def main():
    print(balanced_parentheses_checker('((()))'))
    print(balanced_parentheses_checker('(()'))


if __name__ == "__main__":
    main()
