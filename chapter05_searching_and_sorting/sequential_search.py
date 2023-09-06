# Sequential search (aka linear search): starting at the first item in the list, we move from item to item, following
# the underlying sequential ordering until we either find what we are looking for or run out of items.

# Sequential search of an unordered list. Time is O(n).
def sequential_search_of_unordered_list(unordered_list, item):
    position = 0
    found = False

    while position < len(unordered_list) and not found:
        if unordered_list[position] == item:
            found = True
        else:
            position = position + 1

    return found


# Sequential search of an ordered list. Time is O(n).
def sequential_search_of_ordered_list(ordered_list, item):
    position = 0
    found = False
    stop = False
    while position < len(ordered_list) and not found and not stop:
        if ordered_list[position] == item:
            found = True
        else:
            if ordered_list[position] > item:
                stop = True
            else:
                position = position + 1

    return found


def main():
    unordered_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search_of_unordered_list(unordered_list, 3))
    print(sequential_search_of_unordered_list(unordered_list, 13))

    ordered_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(sequential_search_of_ordered_list(ordered_list, 3))
    print(sequential_search_of_ordered_list(ordered_list, 13))


if __name__ == "__main__":
    main()
