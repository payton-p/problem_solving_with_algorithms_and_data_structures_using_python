# Binary search of an ordered list. Time is O(log(n)).
def binary_search(ordered_list, item):
    first = 0
    last = len(ordered_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if ordered_list[midpoint] == item:
            found = True
        else:
            if item < ordered_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def main():
    ordered_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binary_search(ordered_list, 3))
    print(binary_search(ordered_list, 13))


if __name__ == "__main__":
    main()
