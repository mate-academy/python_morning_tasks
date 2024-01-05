from number_of_recent_calls import RecentCounter


def test_single_ping():
    counter = RecentCounter()
    assert counter.ping(1) == 1


def test_two_pings():
    counter = RecentCounter()
    counter.ping(1)
    assert counter.ping(100) == 2


def test_three_pings():
    counter = RecentCounter()
    counter.ping(1)
    counter.ping(100)
    assert counter.ping(3001) == 3


def test_multiple_non_intersecting_pings():
    counter = RecentCounter()
    assert counter.ping(1) == 1
    assert counter.ping(100) == 2
    assert counter.ping(3001) == 3
    assert counter.ping(3002) == 3
    assert counter.ping(3003) == 4


def test_multiple_intersecting_pings():
    counter = RecentCounter()
    assert counter.ping(100) == 1
    assert counter.ping(200) == 2
    assert counter.ping(2500) == 3
    assert counter.ping(3000) == 4


def test_ping_at_boundary():
    counter = RecentCounter()
    assert counter.ping(100) == 1
    assert counter.ping(3100)


def test_ping_beyond_boundary():
    counter = RecentCounter()
    assert counter.ping(100) == 1
    assert counter.ping(3101) == 1


def test_pings_with_large_gaps():
    counter = RecentCounter()
    assert counter.ping(100) == 1
    assert counter.ping(5000) == 1
    assert counter.ping(10000) == 1
