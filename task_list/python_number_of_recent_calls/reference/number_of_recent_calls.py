from bisect import bisect_right


class RecentCounter:
    def __init__(self) -> None:
        self.requests = []

    def ping(self, time: int) -> int:
        self.requests.append(time)
        last_request = bisect_right(self.requests, time - 3001)
        return len(self.requests) - last_request
