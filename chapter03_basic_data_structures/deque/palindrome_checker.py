from chapter03_basic_data_structures.deque.deque import Deque


# Check if the given string is a palindrome. A palindrome is a word, sentence, verse, or even number that reads the
# same backward as forward.
def palindrome_checker(string_to_check):
    character_deque = Deque()

    # Add each character of the given string to the deque.
    for char in string_to_check:
        character_deque.add_rear(char)

    # Compare the front and rear items in the deque to see if they are equal.
    is_equal = True
    while character_deque.size() > 1 and is_equal:
        first = character_deque.remove_front()
        last = character_deque.remove_rear()

        if first != last:
            is_equal = False

    if is_equal:
        print("\"" + string_to_check + "\"", "is a palindrome.")
    else:
        print("\"" + string_to_check + "\"", "is not a palindrome.")


def main():
    palindrome_checker("radar")
    palindrome_checker("silly")


if __name__ == "__main__":
    main()
