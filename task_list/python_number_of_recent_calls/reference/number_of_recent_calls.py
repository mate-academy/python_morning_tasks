from bisect import bisect_right


class RecentCounter:
    def __init__(self) -> None:
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        last_request = bisect_right(self.requests, t - 3001)
        return len(self.requests) - last_request
