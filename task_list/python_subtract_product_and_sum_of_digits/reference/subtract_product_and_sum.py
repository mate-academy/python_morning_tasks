def subtract_product_and_sum(num: int) -> int:
    sums, product = 0, 1

    while num != 0:
        last_digit = num % 10
        product *= last_digit
        sums += last_digit
        num //= 10

    return product - sums
