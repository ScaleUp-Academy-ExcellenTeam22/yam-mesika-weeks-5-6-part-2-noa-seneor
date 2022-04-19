import time


def fast_and_reliable(path):
    """
    :param path: path of words text file
    The function generates a list and a set of the words from the given path's file,
    and then prints the average time for searching a given word in those data structures
    """
    with open(path) as file:
        words_list = [line.strip() for line in file]
        words_set = set(words_list)
    print(f" list average search time: {average_time(words_list)}")
    print(f" set average search time : {average_time(words_set)}")


def average_time(words_list):
    """
    :param words: set or list of words
    :return: average time to search the word zwitterion in set or list
    """
    total_time = 0
    for i in range(1000):
        starting_time = time.time()
        if 'zwitterion' in words_list:
            pass
        ending_time = time.time()
        total_time += ending_time - starting_time
    return total_time/1000


if __name__ == '__main__':
    fast_and_reliable(r'C:\Users\noase\source\repos\words.txt')




