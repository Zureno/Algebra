"""
Calulating the mode
"""

from collections import Counter


def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]


def calculate_multiple_modes(numbers):
    c = Counter(numbers)
    number_freq = c.most_common()
    max_count = number_freq[0][1]

    modes = []
    for num in number_freq:
        if num[1] == max_count:
            modes.append(num[0])
        return modes


if __name__ == "__main__":
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    score = [5,5,5,4,4,4,9,1,3]
    mode = calculate_mode(scores)
    modes = calculate_multiple_modes(score)
    print("The mode of the list of numbers is: {0}".format(mode))
    print("The mode(s) of the list of numbers are:")
    for mode in modes:
        print(mode)
