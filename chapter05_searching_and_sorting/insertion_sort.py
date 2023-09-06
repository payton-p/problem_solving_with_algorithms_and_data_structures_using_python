# Insertion sort maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back
# into the previous sublist such that the sorted sublist is one item larger. Time is is O(n^2).
def insertion_sort(unordered_list):
    for index in range(1, len(unordered_list)):
        current_value = unordered_list[index]
        
        position = index
        while position > 0 and unordered_list[position - 1] > current_value:
            unordered_list[position] = unordered_list[position - 1]
            position = position - 1

        unordered_list[position] = current_value


def main():
    example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(example_list)
    print(example_list)


if __name__ == "__main__":
    main()
