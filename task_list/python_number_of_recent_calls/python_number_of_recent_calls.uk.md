Реалізуйте клас `RecentCounter`, який підраховує кількість останніх запитів протягом певного періоду часу.

* `RecentCounter()` Створює екземпляр класу, до якого ще не було здійснено жодного запиту.
* `RecentCounter.ping(self, time: int) -> ` Додає новий запит у час `time`, де `time` представляє деякий час у мілісекундах, і повертає кількість запитів, які відбулися за останні 3000 мілісекунд (включаючи новий запит). Іншими словами, повертає кількість запитів, які відбулися у діапазоні `[time - 3000, time]` включно.


**Гарантовано**, що кожен виклик ping використовує строго більше значення t, ніж попередній виклик.

Приклад:
```python
recentCounter = RecentCounter()
recentCounter.ping(1)  # requests = [1], range is [-2999,1], returns 1
recentCounter.ping(100)  # requests = [1, 100], range is [-2900,100], returns 2
recentCounter.ping(3001)  # requests = [1, 100, 3001], range is [1,3001], returns 3
recentCounter.ping(3002)  # requests = [1, 100, 3001, 3002], range is [2,3002], returns 3
```
