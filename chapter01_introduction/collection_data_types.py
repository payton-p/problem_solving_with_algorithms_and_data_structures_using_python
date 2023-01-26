def main():
    # Built-in collection data types.

    # Lists, strings, and types are ordered collections.
    list_example = [2, 5, 2, 8, True, "hey"]  # lists are mutable
    print(list_example)
    string_example = "Hey"  # strings are immutable
    print(string_example)
    tuple_example = (2, 3, 1, "Hello")  # tuples are immutable
    print(tuple_example)

    # When using the repetition operator on a list, the result is a repetition of references to the data objects in the
    # sequence. This is illustrated below.
    my_list = [1, 2, 3, 4]
    other_list = [my_list] * 3
    print(other_list)
    my_list[2] = 45
    print(other_list)
    squared_list = [x * x for x in range(1, 11) if x % 2 != 0]  # example of list comprehension with selection criteria
    print(squared_list)

    # Sets and dictionaries are unordered collections.
    # Sets are a collection of zero or more immutable data objects. Sets do not allow duplicates.
    set_example1 = {3, 5, "dog", True}
    set_example2 = {2, 3, 1}
    print(set_example1)
    union = set_example1.union(set_example2)  # union of sets
    print(union)
    union = set_example1 | set_example2  # another way of getting the union
    print(union)
    intersection = set_example1.intersection(set_example2)  # intersection of sets
    print(intersection)  # 1 is included because 1 and True are seen as equal
    intersection = set_example1 & set_example2  # another way of getting the intersection
    print(intersection)

    # Dictionaries are collections of associated pairs of items where each pair consists of a key and a value.
    dictionary_example = {"Montana": "MT", "Maine": "ME"}  # dictionaries are mutable
    print(dictionary_example)
    print(dictionary_example["Montana"])


if __name__ == "__main__":
    main()
