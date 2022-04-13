def perfect_roll():
    """
    Function that generates perfect numbers infinitely
    Perfect number : a positive integer that is equal to the sum of its proper divisors
    :return: generator of perfect numbers
    """
    # starting from 6 because smallest perfect number is 6
    perfect_num = 6
    while True:
        if perfect_num == sum([x for x in range(1, perfect_num//2 + 1) if perfect_num % x == 0]):
            yield perfect_num
        perfect_num += 1


def main():
    perfect_roll_generator = perfect_roll()
    for perfect in perfect_roll_generator:
        print(perfect)


if __name__ == '__main__':
    main()
