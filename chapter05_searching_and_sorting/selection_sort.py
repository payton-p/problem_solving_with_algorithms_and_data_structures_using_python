# The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order
# to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it
# in the proper location. Selection sort is O(n^2).
def selection_sort(unordered_list):
    for fill_slot in range(len(unordered_list) - 1, 0, -1):
        position_of_max = 0
        for position in range(1, fill_slot + 1):
            if unordered_list[position] > unordered_list[position_of_max]:
                position_of_max = position

        temp = unordered_list[fill_slot]
        unordered_list[fill_slot] = unordered_list[position_of_max]
        unordered_list[position_of_max] = temp


def main():
    example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(example_list)
    print(example_list)


if __name__ == "__main__":
    main()
