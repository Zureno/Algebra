""" Calculating the median """


def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()
    # Find the median
    if N % 2 == 0:
        m1 = N / 2
        m2 = (N / 2) + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        med = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N + 1) / 2
        # Convert to integer, match position
        m = int(m) - 1
        med = numbers[m]
    return med


if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = calculate_median(donations)
    N = len(donations)
    print("Median donation over the last {0} days is {1}".format(N, median))
