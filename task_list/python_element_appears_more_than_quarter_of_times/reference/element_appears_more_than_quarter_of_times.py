from collections import Counter


def find_integer(num_list: list[int]) -> int:
    num_list = Counter(num_list).most_common()

    return num_list[0][0]
