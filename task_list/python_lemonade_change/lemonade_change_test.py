from lemonade_change import sell_lemonade


def test_base_case():
    queue = [5, 5, 5, 10, 20]
    expected = True

    result = sell_lemonade(queue)
    assert result == expected, f"Failed: Should return {expected} for queue = {queue}"

    queue = [5, 5, 10, 10, 20]
    expected = False

    result = sell_lemonade(queue)
    assert (
        result == expected
    ), f"Failed: Can not return change to customer with 20$ bill for queue = {queue}"


def test_single_client():
    queue = [5]
    expected = True

    result = sell_lemonade(queue)
    assert (
        result == expected
    ), f"Failed: Should be able to sell for queue = {queue} there is no change required."


def test_no_fives_to_serve_clients():
    queue = [10, 20]
    expected = False

    result = sell_lemonade(queue)
    assert (
        result == expected
    ), f"Failed: No small banknots to start selling lemo. Queue = {queue} can not be done."

    queue = [20, 5]
    expected = False

    result = sell_lemonade(queue)
    assert result == expected, f"Failed: No change for customers from queue = {queue}."


def test_busy_day_with_many_customers():
    queue = [5, 5, 5, 10, 5, 20, 5, 10, 5, 20]
    expected = True

    result = sell_lemonade(queue)
    assert (
        result == expected
    ), f"Failed: Amount of earned bills is enough to serve all clients for queue = {queue}"


def test_return_only_fives_for_change():
    queue = [5, 5, 5, 5, 20, 5, 10, 5, 5, 20]
    expected = True

    result = sell_lemonade(queue)
    assert (
        result == expected
    ), f"Failed: Should be able to return change with only fives for queue = {queue}"
