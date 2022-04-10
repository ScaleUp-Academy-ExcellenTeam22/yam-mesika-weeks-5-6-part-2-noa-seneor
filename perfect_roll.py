def perfect_roll():
    """
    function that generates perfect numbers infinitely
    :return: generator of perfect number
    """
    i = 6
    while True:
        if i == sum([x for x in range(1, i//2 + 1) if i % x == 0]):
            yield i
        i += 1


def main():
    perfect_roll_generator = perfect_roll()
    for perfect in perfect_roll_generator:
        print(perfect)


if __name__ == '__main__':
    main()