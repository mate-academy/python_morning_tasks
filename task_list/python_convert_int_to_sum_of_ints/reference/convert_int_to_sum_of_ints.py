def convert_into_sum(num: int) -> list[int]:
    def check_zeros(value: int) -> bool:
        while value > 0:
            if value % 10 == 0:
                return False
            value //= 10
        return True

    for integer in range(1, num):
        diff = num - integer
        if check_zeros(diff) and check_zeros(integer):
            return [diff, integer]
