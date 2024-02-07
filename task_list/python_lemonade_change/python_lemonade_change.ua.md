У лимонадних кіосках кожен лимонад коштує `$5`. Клієнти стоять у черзі, щоб за покупкою і замовляють по-одному (порядок визначений банкнотами). Кожен клієнт купує лише один лимонад. Оплата робиться банкнотами, можливі номінали наступні: `$5`, `$10`, або `$20`. Тобі ж необхідно повернути правильну решту кожному клієнту, знаючи, що за лимонад повинно бути сплачено рівно `$5`.

Зауваж, що до перших покупок у тебе на руках взагалі немає готівки.

На вхід дається список з цілих чисел `bills`, де `bills[i]` це банкнота, якою хоче сплатити $i^{ий}$ клієнт. Поверни `True`, якщо зможеш надати правильну решту **кожному клієнту**, в іншому випадку - `False`.

### Приклад 1:
```python
    Input: bills = [5, 5, 5, 10, 20]
    Output: True
```
**_Пояснення_**:
<em>
- З перших 3 клієнтів ми отримуємо три купюри по `5$`;
- З четвертого клієнта отримуємо купюру номіналом у `$10`. Решта `$5`;
- Від п'ятого клієнта ми отримуємо `$10`. Решта знову `$5`;
- Оскільки кожен клієнт отримав коректну решту, повертаємо `True`.
</em>

### Приклад 1:
```python
Input: bills = [5, 5, 10, 10, 20]
Output: False
```
**_Пояснення_**:
<em>
- Отримуємо по `5$` з перших двох клієнтів;
- Ще два наступних приносять нам по банкноті в `$10`, однак щоразу повертажмо решту - `$5`;
- Щодо останнього клієнта - він приносить купюру в `20$` і на цей раз ми вже не можемо повернути йому правильну решту в `$15`, адже у нас залишились лише 2 банкноти номіналом по `10$` кожна;
- Очевидно, що ми б не змогли віддати усім правильну суму, тому функція повинна повернути `False`.
</em>

**_Обмеження_**:
- 1 <= `len(bills)` <= 105
- `bills[i]` може бути наступних номіналів: `5$`, `10$`, or `20$`