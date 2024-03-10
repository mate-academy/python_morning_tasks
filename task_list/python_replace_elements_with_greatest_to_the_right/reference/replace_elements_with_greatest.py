def replace_elements(num_list: list[int]) -> list[int]:
    result = [-1]
    greatest = 0

    for num in num_list[::-1]:
        if greatest < num:
            greatest = num
        result.append(greatest)
    result.pop()
    return result[::-1]
