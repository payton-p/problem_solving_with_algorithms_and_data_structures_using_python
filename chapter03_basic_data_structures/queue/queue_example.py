from chapter03_basic_data_structures.queue.queue import Queue


def main():
    print("Queue example.")

    queue = Queue()
    print("Is empty:", queue.is_empty())

    queue.enqueue(3)
    queue.enqueue(2)
    print("Queue:", queue.items)
    print("Size:", queue.size())
    print("Is empty:", queue.is_empty())

    queue.dequeue()
    print("Queue:", queue.items)


if __name__ == "__main__":
    main()
