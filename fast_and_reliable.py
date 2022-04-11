import time


def fast_and_reliable(path):
    """
    :param path: path of words text file
    generate list and set of words from path and print
    average time to search a word in the list vs in the set
    """
    with open(path) as f:
        words_list = [line.strip() for line in f]
        words_set = set(words_list)
    print(f" list average search time: {average_time(words_list)}")
    print(f" set average search time : {average_time(words_set)}")


def average_time(words):
    """
    :param words: set or list of words
    :return: average time to search the word zwitterion in set or list
    """
    total_time = 0
    for i in range(1000):
        while True:
            starting_time = time.time()
            if 'zwitterion' in words:
                ending_time = time.time()
                break
        total_time += ending_time - starting_time
    return total_time/1000


if __name__ == '__main__':
    fast_and_reliable(r'C:\Users\noase\source\repos\words.txt')

