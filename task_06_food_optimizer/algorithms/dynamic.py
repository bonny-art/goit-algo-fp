"""
Ця програма реалізує динамічне програмування для вирішення задачі вибору предметів 
(наприклад, продуктів харчування) із заданими вартістю та калоріями таким чином, 
щоб максимізувати кількість калорій, не перевищуючи заданий бюджет.

Функція dynamic_programming приймає словник предметів, де кожен предмет має 
вказані "cost" (вартість) та "calories" (кількість калорій), а також бюджет. 
Вона повертає список вибраних предметів, загальну вартість та максимальну кількість калорій.
"""

from typing import Dict, Tuple, List

def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[List[str], int, int]:
    """
    Знаходить список предметів із максимальним рівнем калорій за обмеженого бюджету.

    Аргументи:
        items (Dict[str, Dict[str, int]]): Словник, де ключами є назви предметів, а значеннями — 
        вкладені словники з полями "cost" (вартість) та "calories" (калорії).
        budget (int): Максимальна доступна сума грошей (бюджет).

    Повертає:
        Tuple[List[str], int, int]: Кортеж, що містить список вибраних предметів, 
        загальну вартість та максимальну кількість калорій.
    """
    n = len(items)
    item_list = list(items.items())

    # Ініціалізуємо таблицю dp для зберігання максимальних калорій для кожного бюджету
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        item_name, data = item_list[i - 1]
        cost, calories = data['cost'], data['calories']
        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    # Відновлюємо вибрані предмети, вартість та калорії
    selected_items = []
    total_cost = 0
    total_calories = dp[n][budget]
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name = item_list[i - 1][0]
            selected_items.append(item_name)
            total_cost += items[item_name]['cost']
            j -= items[item_name]['cost']

    # Виводимо список предметів у правильному порядку
    selected_items.reverse()
    return selected_items, total_cost, total_calories
