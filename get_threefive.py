

def get_threefive(start, end):
    """
    Returns list of values for the range of integers from start to end. If the number is divisible by three, then in the
    list will be string "Three". If the number is divisible by five, then in the list will be string "Five". If the
    number is divisible both by three and five, then in the list will be the string "ThreeFive".
    :param start: first number
    :param end: last number (inclusive)
    :return: list of integers or strings according to the algorithm
    """
    result = []
    for num in range(start, end + 1):
        if num % 5 == 0 and num % 3 == 0:
            num = "ThreeFive"
        elif num % 5 == 0:
            num = "Five"
        elif num % 3 == 0:
            num = "Three"

        result.append(num)
    return result


if __name__ == '__main__':
    numbers = get_threefive(1, 100)
    for num in numbers:
        print(num)
