# These definitions were largely taken from:
# https://runestone.academy/ns/books/published/pythonds/SortSearch/TheQuickSort.html
# Review that link for additional details.

# The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional
# storage. As a trade-off, however, it is possible that the list may not be divided in half. When this happens, we will
# see that performance is diminished.

# A quick sort first selects a value, which is called the pivot value. Although there are many ways to choose the pivot
# value, we will simply use the first item in the list. The role of the pivot value is to assist with splitting the
# list. The actual position where the pivot value belongs in the final sorted list, commonly called the split point,
# will be used to divide the list for subsequent calls to the quick sort.

# The partition process will happen next. It will find the split point and at the same time move other items to the
# appropriate side of the list, either less than or greater than the pivot value.

# Partitioning begins by locating two position markers, at the beginning and end of the remaining items in the list.
# The goal of the partition process is to move items that are on the wrong side with respect to the pivot value while
# also converging on the split point.

# We begin by incrementing left mark until we locate a value that is greater than the pivot value. We then decrement
# right mark until we find a value that is less than the pivot value. At this point we have discovered two items that
# are out of place with respect to the eventual split point. Now we can exchange these two items and then repeat the
# process again.

# At the point where right mark becomes less than left mark, we stop. The position of right mark is now the split point.
# The pivot value can be exchanged with the contents of the split point and the pivot value is now in place. In
# addition, all the items to the left of the split point are less than the pivot value, and all the items to the right
# of the split point are greater than the pivot value. The list can now be divided at the split point and the quick sort
# can be invoked recursively on the two halves.

# We can attempt to alleviate some of the potential for an uneven division by using a technique called median of three.
# To choose the pivot value, we will consider the first, the middle, and the last element in the list. In our example,
# those are 54, 77, and 20. Now pick the median value, in our case 54, and use it for the pivot value (of course, that
# was the pivot value we used originally). The idea is that in the case where the first item in the list does not belong
# toward the middle of the list, the median of three will choose a better “middle” value. This will be particularly
# useful when the original list is somewhat sorted to begin with.

# A quick sort is O(nlog(n)), but may degrade to O(n^2) if the split points are not near the middle of the list. It does
# not require additional space.
def quick_sort(unordered_list):
    quick_sort_helper(unordered_list, 0, len(unordered_list) - 1)


def quick_sort_helper(unordered_list, first, last):
    if first < last:
        split_point = partition(unordered_list, first, last)

        quick_sort_helper(unordered_list, first, split_point - 1)
        quick_sort_helper(unordered_list, split_point + 1, last)


def partition(unordered_list, first, last):
    pivot_value = unordered_list[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and unordered_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while unordered_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = unordered_list[left_mark]
            unordered_list[left_mark] = unordered_list[right_mark]
            unordered_list[right_mark] = temp

    temp = unordered_list[first]
    unordered_list[first] = unordered_list[right_mark]
    unordered_list[right_mark] = temp

    return right_mark


def main():
    example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(example_list)
    print(example_list)


if __name__ == "__main__":
    main()
