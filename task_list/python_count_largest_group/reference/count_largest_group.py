from collections import defaultdict, Counter


def count_largest_group(number: int) -> int:
    mapper = defaultdict(list)

    for num in range(1, number + 1):
        temp = num
        count = 0

        while temp != 0:
            count += temp % 10
            temp //= 10

        mapper[count].append(num)

    lengths = Counter(len(value) for value in mapper.values())
    result = lengths.get(max(lengths))

    return result
