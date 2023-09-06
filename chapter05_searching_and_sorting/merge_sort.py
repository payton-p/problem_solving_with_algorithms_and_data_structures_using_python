# Merge sort is a divide and conquer strategy. Merge sort is a recursive algorithm that continually splits a list in
# half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one
# item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the
# fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and
# combining them together into a single, sorted, new list. Merge sort is O(nlog(n), but requires additional space for
# the merging process.
def merge_sort(unordered_list):
    print("Splitting ", unordered_list)

    if len(unordered_list) > 1:
        mid = len(unordered_list) // 2
        left_half = unordered_list[:mid]
        right_half = unordered_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                unordered_list[k] = left_half[i]
                i = i + 1
            else:
                unordered_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            unordered_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            unordered_list[k] = right_half[j]
            j = j + 1
            k = k + 1

    print("Merging ", unordered_list)


def main():
    example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(example_list)
    print(example_list)


if __name__ == "__main__":
    main()
