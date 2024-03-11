def sum_zero(number: int) -> list[int]:
    result_list = [0] if number % 2 else []

    for num in range(1, number // 2 + 1):
        result_list.append(num)
        result_list.append(-num)

    return result_list
