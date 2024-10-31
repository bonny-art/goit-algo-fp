"""
Ця програма симулює кидання двох гральних кубиків для підрахунку ймовірностей випадіння різних сум.
Функція `simulate_dice_rolls` дозволяє обчислити ймовірності випадіння кожної можливої суми для
заданої кількості кидків.
"""

import random

def simulate_dice_rolls(num_rolls: int, seed: int = None) -> dict[int, float]:
    """
    Симулює кидання двох гральних кубиків для підрахунку ймовірностей випадіння кожної суми.

    Параметри:
        num_rolls (int): Кількість кидків кубиків.
        seed (int, optional): Початкове значення для генератора випадкових чисел. 

    Повертає:
        dict[int, float]: Словник ймовірностей випадіння кожної суми від 2 до 12.
    """
    if seed is not None:
        random.seed(seed)  # Встановлює початкове значення для генератора випадкових чисел

    # Ініціалізує словник для підрахунку сум
    sum_counts = {i: 0 for i in range(2, 13)}

    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1  # Підрахунок випадіння кожної суми

    # Розрахунок ймовірностей
    probabilities = {k: v / num_rolls for k, v in sum_counts.items()}
    return probabilities
