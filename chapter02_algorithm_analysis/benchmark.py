import time


# You can benchmark a function by noting the start and end time, and calculating the difference. A benchmark tests the
# time of execution.
def main():
    start = time.time()

    sum_example = 0
    for i in range(1000000):
        sum_example += i

    end = time.time()

    print("Time in seconds: ", end - start)


if __name__ == "__main__":
    main()
