import timeit


# T(n) is the time it takes to solve a problem of size n. The order of magnitude function describes the part of T(n)
# that increases the fastest as the value of n increases. Order of magnitude is often called Big-O notation and written
# as O(f(n)). It provides a useful approximation to the actual number of steps in the computation.

# Append example.
def append_test(list_example, item):
    list_example.append(5)


# Concatenate example.
def concatenate_test(list_example, another_list):
    list_example = list_example + another_list


def main():
    list_example = list(range(1000))

    # Capture the time it takes for the function to execute. The timeit module is designed to make cross-platform
    # timing measurements by running functions in a consistent environment and using timing mechanisms that are as
    # similar as possible across operating systems.
    t1 = timeit.Timer(lambda: append_test(list_example, 5))  # by default timeit will run 1 million times
    print("Append:", t1.timeit(number=1000), "milliseconds")  # appending to a list is O(1)

    # Concatenating lists is O(k), where k is the size of the list that is being concatenated.
    another_list = [6, 7, 8]
    t2 = timeit.Timer(lambda: concatenate_test(list_example, another_list))
    print("Concatenate:", t2.timeit(number=1000), "milliseconds")


if __name__ == "__main__":
    main()
