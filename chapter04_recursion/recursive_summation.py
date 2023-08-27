def find_summation(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + find_summation(num_list[1:])


def main():
    print(find_summation([1, 3, 5, 7, 9]))


if __name__ == "__main__":
    main()
