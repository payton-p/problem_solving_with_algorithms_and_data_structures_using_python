# The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of
# order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles”
# up to the location where it belongs. Bubble sort is O(n^2).

# A bubble sort can be modified to stop early if it finds that the list has become sorted. This is often referred to as
# the short bubble.
def short_bubble_sort(unordered_list):
    exchanges = True

    position = len(unordered_list) - 1
    while position > 0 and exchanges:
        exchanges = False
        for i in range(position):
            if unordered_list[i] > unordered_list[i + 1]:
                exchanges = True
                temp = unordered_list[i]
                unordered_list[i] = unordered_list[i + 1]
                unordered_list[i + 1] = temp

        position = position - 1


def main():
    example_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    short_bubble_sort(example_list)
    print(example_list)


if __name__ == "__main__":
    main()
