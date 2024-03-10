# def find_integer(num_list: list[int]) -> int:
#     pass
def find_integer(num_list: list[int]) -> int:
    if len(num_list) <= 2:
        return num_list[0]

    target = len(num_list) // 4
    result_mapper = {}

    for num in num_list:
        if num in result_mapper:
            result_mapper[num] += 1
            if result_mapper.get(num) > target:
                return num
            continue
        result_mapper[num] = 1

    return max(result_mapper, key=result_mapper.get)
