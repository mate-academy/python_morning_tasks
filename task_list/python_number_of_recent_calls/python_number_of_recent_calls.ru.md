You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

* `RecentCounter()` Initializes the counter with zero recent requests.
* `RecentCounter.ping(self, time: int) -> ` Adds a new request at time `time`, where `time` represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[time - 3000, time]`. 


It is **guaranteed** that every call to ping uses a strictly larger value of t than the previous call.


Example :
```python
recentCounter = RecentCounter()
recentCounter.ping(1)  # requests = [1], range is [-2999,1], returns 1
recentCounter.ping(100)  # requests = [1, 100], range is [-2900,100], returns 2
recentCounter.ping(3001)  # requests = [1, 100, 3001], range is [1,3001], returns 3
recentCounter.ping(3002)  # requests = [1, 100, 3001, 3002], range is [2,3002], returns 3
```
