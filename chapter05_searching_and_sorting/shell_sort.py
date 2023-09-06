# The shell sort, sometimes called the “diminishing increment sort,” improves on the insertion sort by breaking the
# original list into a number of smaller sublists, each of which is sorted using an insertion sort. The unique way that
# these sublists are chosen is the key to the shell sort. Instead of breaking the list into sublists of contiguous
# items, the shell sort uses an increment i, sometimes called the gap, to create a sublist by choosing all items that
# are i items apart. In general, shell sort tends to fall somewhere between O(n) and O(n^2).
def shell_sort(unordered_list):
    sublist_count = len(unordered_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(unordered_list, start_position, sublist_count)

        print("After increments of size", sublist_count, "the list is", unordered_list)

        sublist_count = sublist_count // 2


def gap_insertion_sort(unordered_list, start, gap):
    for i in range(start + gap, len(unordered_list), gap):
        current_value = unordered_list[i]

        position = i
        while position >= gap and unordered_list[position - gap] > current_value:
            unordered_list[position] = unordered_list[position - gap]
            position = position - gap

        unordered_list[position] = current_value


def main():
    example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(example_list)
    print(example_list)


if __name__ == "__main__":
    main()
